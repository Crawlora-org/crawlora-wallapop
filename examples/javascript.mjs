import { WallapopClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new WallapopClient({ apiKey });

  const filters = await client.filters({ q: "bicycle" });
  console.log("filters", filters);
  const categories = await client.categories({  });
  console.log("categories", categories);
