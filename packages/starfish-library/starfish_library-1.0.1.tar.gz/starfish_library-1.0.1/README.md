参考サイト
https://zenn.dev/sikkim/articles/490f4043230b5a

ライブラリの反映手順
setup.py のバージョンを更新
python setup.py sdist で配布物のビルド
python setup.py bdist_wheel Wheelパッケージをビルド

テスト環境にアップロード(依存関係などでエラーが出ないか)
twine upload --repository testpypi dist/*

本番環境にアップロード
twine upload --repository pypi dist/*