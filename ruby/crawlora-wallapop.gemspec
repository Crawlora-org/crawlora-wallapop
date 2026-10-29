require_relative "lib/crawlora/wallapop/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-wallapop"
  spec.version = Crawlora::Wallapop::VERSION
  spec.summary = "Wallapop API client for Crawlora (5 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Wallapop API. Covers public listing search, categories, filters, and item details across 5 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-wallapop", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-wallapop/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
