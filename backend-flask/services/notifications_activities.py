from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware


class NotificationsActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()

    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'Karthik Muraliprasad',
      'message': 'Carpediem !!!',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 5,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Worf',
        'message': 'This post has no honor!',
        'likes_count': 0,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }],
    },
    {
      'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
      'handle':  'Lionel Messi',
      'message': 'G.O.A.T',
      'created_at': (now - timedelta(days=7)).isoformat(),
      'expires_at': (now + timedelta(days=9)).isoformat(),
      'likes': 0,
      'replies': []
    },
    ]

    # subsegment = xray_recorder.begin_segment('notifications-activities-mock-data')

    # data = {
    #   "now": now.isoformat(),
    #   "results-size": len(results)
    # }

    # subsegment.put_metadata('key', data, 'metadata')
    # xray_recorder.end_subsegment()

    return results
