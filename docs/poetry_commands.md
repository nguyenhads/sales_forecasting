## POETRY COMMANDS

| COMMAND                | MEANING                                             | EXAMPLE                                        |
|------------------------|-----------------------------------------------------|-----------------------------------------------|
| poetry new             | Tạo một dự án mới.                                  | poetry new project_name                       |
| poetry init            | Tạo một tệp pyproject.toml mới cho dự án tồn tại. | poetry init                                   |
| poetry install         | Cài đặt dependencies từ pyproject.toml.           | poetry install                               |
| poetry add             | Thêm một gói vào danh sách dependencies.            | poetry add package_name                      |
| poetry add --dev       | Thêm một gói cho mục đích phát triển.              | poetry add --dev package_name               |
| poetry remove          | Gỡ bỏ một gói khỏi danh sách dependencies.        | poetry remove package_name                   |
| poetry update          | Cập nhật tất cả các dependencies đến phiên bản mới. | poetry update                                |
| poetry build           | Xây dựng gói Python từ mã nguồn dự án.              | poetry build                                 |
| poetry publish         | Đăng gói lên PyPI.                                  | poetry publish                               |
| poetry config          | Cấu hình Poetry.                                    | poetry config setting_name value            |
| poetry run             | Chạy một lệnh Python hoặc lệnh cài đặt.            | poetry run python script.py                 |
| poetry shell           | Mở một môi trường shell với dependencies của dự án. | poetry shell                                |
| poetry check           | Kiểm tra xem dự án có vấn đề gì không.            | poetry check                                  |
| poetry show            | Hiển thị thông tin về các dependencies.            | poetry show                                   |
| poetry search          | Tìm kiếm gói trên PyPI.                            | poetry search package_name                   |
| poetry self-update     | Cập nhật Poetry lên phiên bản mới nhất.           | poetry self-update                            |
| poetry env info        | Hiển thị thông tin về môi trường virtualenv.      | poetry env info                               |
| poetry config --list   | Hiển thị tất cả các cấu hình.                      | poetry config --list                          |
| poetry lock            | Tạo một tệp poetry.lock dựa trên pyproject.toml.   | poetry lock                                   |
| poetry export          | Tạo một tệp requirements.txt từ pyproject.toml.    | poetry export --format requirements.txt      |
| poetry run <command>   | Chạy một lệnh được cài đặt bởi dependencies.     | poetry run python script.py                  |
| poetry build --format  | Xây dựng gói theo một định dạng cụ thể.           | poetry build --format wheel                  |
| poetry config --unset  | Gỡ bỏ một cấu hình cụ thể.                        | poetry config --unset setting_name           |
