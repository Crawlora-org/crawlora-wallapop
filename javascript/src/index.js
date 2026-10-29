import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class WallapopClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-wallapop-js/0.1.0" });
    this["categories"] = (...args) => this.request("wallapop-categories", ...args);
    this["filterOptions"] = (...args) => this.request("wallapop-filter-options", ...args);
    this["filters"] = (...args) => this.request("wallapop-filters", ...args);
    this["itemDetail"] = (...args) => this.request("wallapop-item-detail", ...args);
    this["search"] = (...args) => this.request("wallapop-search", ...args);
  }
}

export { WallapopClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default WallapopClient;
