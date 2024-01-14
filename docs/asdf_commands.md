## ASDF COMMANDS
| COMMAND               | MEANING                                        | EXAMPLE                                       |
|-----------------------|------------------------------------------------|-----------------------------------------------|
| asdf plugin-add        | Thêm một plugin vào asdf.                      | asdf plugin-add python https://github.com/danhper/asdf-python.git |
| asdf plugin-list       | Hiển thị danh sách các plugin đã cài đặt.     | asdf plugin-list                              |
| asdf plugin-update     | Cập nhật một plugin đã cài đặt.                | asdf plugin-update python                    |
| asdf install          | Cài đặt một phiên bản cụ thể của một ngôn ngữ hoặc công cụ. | asdf install python 3.8.5                    |
| asdf global           | Đặt một phiên bản cụ thể làm phiên bản toàn cầu. | asdf global python 3.8.5                     |
| asdf local            | Đặt một phiên bản cụ thể làm phiên bản cục bộ. | asdf local python 3.8.5                      |
| asdf current          | Hiển thị phiên bản đang được sử dụng hiện tại. | asdf current python                          |
| asdf list             | Hiển thị tất cả các phiên bản đã cài đặt.     | asdf list python                             |
| asdf uninstall        | Gỡ bỏ một phiên bản đã cài đặt.               | asdf uninstall python 3.8.5                  |
| asdf where            | Hiển thị đường dẫn đến thư mục cài đặt của phiên bản. | asdf where python                            |
| asdf reshim           | Cập nhật các liên kết symbolic sau khi thêm hoặc xóa một phiên bản. | asdf reshim                                  |
| asdf update           | Cập nhật tất cả các plugin và phiên bản đã cài đặt. | asdf update                                  |
| asdf reshim <version> | Cập nhật liên kết symbolic cho một phiên bản cụ thể. | asdf reshim python 3.8.5                     |
| asdf help             | Hiển thị trợ giúp cho asdf.                    | asdf help                                    |
