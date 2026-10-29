require "json"
require "net/http"
require "uri"

module Crawlora
  module Wallapop
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"wallapop-categories": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-categories", "method": "GET", "params": [], "path": "/wallapop/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "wallapop-filter-options": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-filter-options", "method": "GET", "params": [{"description": "Remote filter ID advertised by /wallapop/filters for this category", "in": "query", "name": "filter_id", "required": true, "type": "string", "x-example": "item_language"}, {"description": "Live category ID from /wallapop/categories. Use a root for brand/model or the selected category for category-specific remote options.", "in": "query", "name": "category_id", "required": true, "type": "integer", "x-example": 24100}, {"description": "Required with filter_id=model; a brand option ID", "in": "query", "name": "brand", "type": "string", "x-example": "BMW"}, {"description": "Optional listing search context", "in": "query", "name": "q", "type": "string", "x-example": "iphone"}, {"description": "Optional listing sort context", "enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string", "x-example": "most_relevance"}, {"description": "Optional text search inside the dynamic option list", "in": "query", "name": "options_query", "type": "string", "x-example": "BMW"}, {"description": "Opaque next_cursor returned by this endpoint", "in": "query", "name": "cursor", "type": "string"}], "path": "/wallapop/filter-options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "filter_id", "required": true, "type": "string"}, {"in": "query", "name": "category_id", "required": true, "type": "integer"}, {"in": "query", "name": "brand", "type": "string"}, {"in": "query", "name": "q", "type": "string"}, {"enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "options_query", "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "wallapop-filters": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-filters", "method": "GET", "params": [{"description": "Optional search phrase used to select relevant filters", "in": "query", "name": "q", "type": "string", "x-example": "iphone"}, {"description": "Any live search taxonomy ID from /wallapop/categories", "in": "query", "name": "category_id", "type": "integer", "x-example": 100}], "path": "/wallapop/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "category_id", "type": "integer"}], "security": ["ApiKeyAuth"]}, "wallapop-item-detail": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-item-detail", "method": "GET", "params": [{"description": "Clean https public item URL from /wallapop/search on es.wallapop.com, it.wallapop.com, or pt.wallapop.com", "in": "query", "name": "url", "required": true, "type": "string", "x-example": "https%3A%2F%2Fes.wallapop.com%2Fitem%2Fchaqueta-1183989904"}], "path": "/wallapop/item", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "wallapop-search": {"bodyParam": null, "bodyRequired": false, "id": "wallapop-search", "method": "GET", "params": [{"description": "Free-text listing search, 2 to 200 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "iphone"}, {"description": "Caller-provided search latitude, -90 through 90", "in": "query", "name": "latitude", "required": true, "type": "number", "x-example": 40.4168}, {"description": "Caller-provided search longitude, -180 through 180", "in": "query", "name": "longitude", "required": true, "type": "number", "x-example": -3.7038}, {"description": "Any live search taxonomy ID from /wallapop/categories", "in": "query", "name": "category_id", "type": "integer", "x-example": 24200}, {"description": "Wallapop sort order", "enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string", "x-example": "most_relevance"}, {"description": "Minimum sale price", "in": "query", "name": "min_price", "type": "number", "x-example": 10}, {"description": "Maximum sale price", "in": "query", "name": "max_price", "type": "number", "x-example": 500}, {"description": "Repeatable or comma-separated condition values. With category_id, use the current values from /wallapop/filters; without category_id, base values are new, as_good_as_new, good, fair, and has_given_it_all.", "in": "query", "name": "condition", "type": "string", "x-example": "new,good"}, {"description": "Pass true to limit to shipping-capable listings; omit to include all. false is rejected because Wallapop ignores it.", "enum": ["true"], "in": "query", "name": "is_shippable", "type": "string", "x-example": "true"}, {"description": "Listing date window", "enum": ["today", "lastWeek", "lastMonth"], "in": "query", "name": "time_filter", "type": "string", "x-example": "lastWeek"}, {"description": "Maximum distance from the supplied coordinates, 0 through 1000 km", "in": "query", "name": "distance_in_km", "type": "integer", "x-example": 25}, {"collectionFormat": "csv", "description": "Repeatable category-specific key:value pair discovered from /wallapop/filters, e.g. brand:BMW, color:Black, has_warranty:true, storage_capacity:128gb, item_language:english, or fashion_size:3,4. For remote values use IDs returned by /wallapop/filter-options.", "in": "query", "items": {"type": "string"}, "name": "filter", "type": "array", "x-example": "storage_capacity:128gb"}, {"description": "Opaque next_cursor returned by a previous response. Use it alone, without initial search parameters.", "in": "query", "name": "cursor", "type": "string", "x-example": "eyJ2IjoxLCJuZXh0X3BhZ2UiOiJ..."}], "path": "/wallapop/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "latitude", "required": true, "type": "number"}, {"in": "query", "name": "longitude", "required": true, "type": "number"}, {"in": "query", "name": "category_id", "type": "integer"}, {"enum": ["closest", "most_relevance", "newest", "price_low_to_high", "price_high_to_low"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "min_price", "type": "number"}, {"in": "query", "name": "max_price", "type": "number"}, {"in": "query", "name": "condition", "type": "string"}, {"enum": ["true"], "in": "query", "name": "is_shippable", "type": "string"}, {"enum": ["today", "lastWeek", "lastMonth"], "in": "query", "name": "time_filter", "type": "string"}, {"in": "query", "name": "distance_in_km", "type": "integer"}, {"collectionFormat": "csv", "in": "query", "name": "filter", "type": "array"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["wallapop-categories", "wallapop-filter-options", "wallapop-filters", "wallapop-item-detail", "wallapop-search"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-wallapop-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('wallapop-categories', params, response_type: response_type)
      end
      define_method('filter_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('wallapop-filter-options', params, response_type: response_type)
      end
      define_method('filters') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('wallapop-filters', params, response_type: response_type)
      end
      define_method('item_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('wallapop-item-detail', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('wallapop-search', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
