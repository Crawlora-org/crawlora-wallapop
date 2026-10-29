import { WallapopClient } from "../src/index.js";

const client = new WallapopClient({ apiKey: "test-key" });
void client.filterOptions({"filter_id": "sample", "category_id": 1});
void client.request("wallapop-filter-options", {"filter_id": "sample", "category_id": 1});
const streamResponse: Promise<Response> = client.request("wallapop-filter-options", {"filter_id": "sample", "category_id": 1}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("wallapop-filter-options", {"filter_id": "sample", "category_id": 1}, { responseType: "stream" });
const directStream: Promise<Response> = client.filterOptions({"filter_id": "sample", "category_id": 1}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("wallapop-filter-options", {"filter_id": "sample", "category_id": 1, "brand": "sample", "q": "sample", "sort": "closest", "options_query": "sample", "cursor": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("wallapop-filter-options", {"filter_id": "sample", "category_id": 1}, { responseType: "text" });
void rawText;


void client.categories();
void client.request("wallapop-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.filterOptions();
