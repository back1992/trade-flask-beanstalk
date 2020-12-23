import logging
import pandas as pd


def get_data_sina(fut_code, exchange):
    try:
        if exchange == "CFFEX":
            url = 'http://stock2.finance.sina.com.cn/futures/api/json.php/%s?symbol=%s0' % (
                'CffexFuturesService.getCffexFuturesDailyKLine',
                fut_code)
        else:
            url = 'http://stock2.finance.sina.com.cn/futures/api/json.php/%s?symbol=%s0' % (
                'IndexService.getInnerFuturesDailyKLine',
                fut_code)
        print(url)
    except:
        logging.error("fut_code")

    else:
        df = pd.read_json(url)
        df = df[-50:]
        # df = df.iloc[::-1]
        return df
