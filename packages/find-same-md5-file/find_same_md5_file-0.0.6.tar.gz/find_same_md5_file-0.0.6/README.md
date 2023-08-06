# find-same-file
[中文文档](https://www.yt-blog.top/58785)

Python searches the same file based on md5
## install
```sh
pip install find-same-md5-file
```
## Example
```python
import find_same_md5_file
# find same file
print(find_same_md5_file.print_same('C:/'))# My U drive letter is U:, so the location is U:/
# find empty dir
print(find_same_md5_file.find_empty_dir('C:/'))
# find big file
print(find_same_md5_file.find_big_file('U:/', 3685))
```
