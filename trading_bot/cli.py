import argparse
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import *
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.qty)
        validate_price(args.price, args.type)

        client = BinanceClient().get_client()
        service = OrderService(client)

        print("\nOrder Request Summary:")
        print(vars(args))

        response = service.place_order(
            args.symbol,
            args.side,
            args.type,
            args.qty,
            args.price
        )

        print("\nOrder Response:")
        print({
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice")
        })

        print("\n✅ Order placed successfully")

    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()