name: Build APK
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libgdbm-dev libncurses5-dev libreadline-gplv2-dev libssl-dev tk-dev libdb5.3-dev libexpat1-dev libffi-dev liblzma-dev
          python -m pip install --upgrade pip
          pip install buildozer cython==0.29.33
      - name: Build with Buildozer
        run: yes | buildozer android debug
      - name: Upload APK
        uses: actions/upload-artifact@v2
        with:
          name: The-Guard-Final-APK
          path: bin/*.apk
