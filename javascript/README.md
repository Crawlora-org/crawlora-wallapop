# @crawlora-org/wallapop — Wallapop API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Wallapop API.
It exposes 5 API endpoints for public listing search, categories, filters, and item details through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-javascript-homepage). It does not run a browser or scrape Wallapop locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Wallapop or its owners.

## Install

```sh
npm install @crawlora-org/wallapop
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=wallapop-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { WallapopClient } from "@crawlora-org/wallapop";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new WallapopClient({ apiKey });
const result1 = await client.filters({ q: "bicycle" });
console.log(result1);
const result2 = await client.categories({});
console.log(result2);
```

The client also exports `Client` as an alias for `WallapopClient`. Operation
methods are available directly in camelCase and through the `wallapop`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Wallapop API endpoints

This package exposes each route below as a direct method and through the `wallapop` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-wallapop/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/wallapop/categories` | `wallapop-categories` | Discover Wallapop search categories |
| `GET` | `/wallapop/filter-options` | `wallapop-filter-options` | Discover Wallapop remote filter values |
| `GET` | `/wallapop/filters` | `wallapop-filters` | Discover Wallapop search filters |
| `GET` | `/wallapop/item` | `wallapop-item-detail` | Fetch a public Wallapop listing detail page |
| `GET` | `/wallapop/search` | `wallapop-search` | Search Wallapop public listings |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
