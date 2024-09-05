def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')

# pytest test/pytest_test.py --help
