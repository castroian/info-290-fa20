test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(test_statistics_under_null) == 10000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 7.5 <= (sum(test_statistics_under_null) / len(test_statistics_under_null)) <= 15
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
