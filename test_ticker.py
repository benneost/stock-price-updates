# import os
# import requests
# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def get_price_change(
#     ticker: str,
#     lookback: Optional[str] = "2d"
# ) -> Tuple[float, List]:
#     """Gets price change for a particular ticker
#     Args:
#         ticker (str): Ticker of interest. E.g., BABA or Y92.SI
#         lookback (str, optional): Price change period to evaluate on.
#             Defaults to "2d".
#     Returns:
#         Tuple[float, List]: Percentage change in float.
#     """
#     stock = yf.Ticker(ticker)
#     hist = stock.history(period=lookback).Close.values.tolist()
#     if len(hist) != int(lookback[0]):
#         lookback = f"{int(lookback[0])+1}d"
#         hist = stock.history(period=lookback).Close.values.tolist()

#     if not hist:
#         return f"Couldn't find history for ticker {ticker}", None
#     pct_chng = ((hist[-1] - hist[0]) / hist[0]) * 100
#     print(np.round(pct_chng, 2), hist)
#     return np.round(pct_chng, 2), hist


# get_price_change("TSLA")


# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)