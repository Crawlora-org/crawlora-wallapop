use crawlora_wallapop::{Client, ModelWallapopFiltersResponseDoc, WallapopFiltersParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .wallapop
        .filters(WallapopFiltersParams {
            q: Some("bicycle".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelWallapopFiltersResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
