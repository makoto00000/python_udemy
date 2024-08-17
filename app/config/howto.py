import logging

logger = logging.getLogger(__name__)

logger.error('Api call is failed')

logger.error({
  'action': 'create',
  'status': 'fail',
  'message': 'Api call is failed'
})

# log解析ソフトなどでkey-value型で解析させる場合
# {'action': 'create', 'status': 'fail', 'message': 'Api call is failed'}

# 関数が呼ばれたとき、raiseの前など、トラブル対応を考えてログを仕込む場所を考える。
