# 📦 Asset & Meeting Room Management System

## Báo cáo dự án ERP - Odoo 15

> **Quản lý Tài sản & Đặt phòng họp**

------------------------------------------------------------------------

# Mục lục

1.  Giới thiệu
2.  Kiến trúc hệ thống
3.  Module chức năng
4.  Cơ sở dữ liệu
5.  Quy trình nghiệp vụ
6.  Tự động hóa quy trình (Mức 2)
7.  Giao diện hệ thống
8.  Biểu đồ minh họa
9.  Kết quả đạt được
10. Hướng phát triển
11. Hướng dẫn cài đặt

------------------------------------------------------------------------

# 1. Giới thiệu

Hệ thống được phát triển trên **Odoo 15** nhằm quản lý tập trung tài
sản, phòng họp và lịch sử sử dụng.

## Mục tiêu

-   Quản lý tài sản
-   Quản lý phòng họp
-   Quản lý lịch đặt
-   Quản lý lịch sử sử dụng
-   Tự động hóa nghiệp vụ
-   Thống kê dữ liệu

------------------------------------------------------------------------

# 2. Kiến trúc hệ thống

``` text
Người dùng
    │
    ▼
 Odoo Web Client
    │
    ▼
 Asset Management Module
    │
 ├── Asset
 ├── Category
 ├── Meeting Room
 ├── Booking
 ├── History
    │
    ▼
 PostgreSQL Database
```

------------------------------------------------------------------------

# 3. Module chức năng

  Module            Mô tả
  ----------------- -------------------
  Quản lý tài sản   CRUD tài sản
  Danh mục          Phân loại tài sản
  Phòng họp         Quản lý phòng
  Đặt phòng         Booking
  Lịch sử           Theo dõi sử dụng

------------------------------------------------------------------------

# 4. Mô hình dữ liệu

``` text
Category
   │1
   │
   │N
Asset
   │1
   ├──────────────┐
   │              │
   ▼              ▼
History       Booking
                  │
                  ▼
            Meeting Room
```

------------------------------------------------------------------------

# 5. Quy trình nghiệp vụ

## Quản lý tài sản

``` text
Tạo tài sản
   ↓
Phân loại
   ↓
Giao nhân viên
   ↓
Đang sử dụng
   ↓
Sửa chữa (nếu có)
   ↓
Thanh lý
```

## Đặt phòng

``` text
Tạo booking
      ↓
Kiểm tra phòng
      ↓
Còn trống?
  ↓         ↓
 Có       Không
  ↓         ↓
Lưu     Thông báo
```

------------------------------------------------------------------------

# 6. Tự động hóa (Mức 2)

### Event 1

Đặt phòng → Kiểm tra trùng lịch → Cho phép/Từ chối

### Event 2

Giao tài sản → Trạng thái chuyển **Đang sử dụng**

### Event 3

Trả tài sản → Trạng thái chuyển **Sẵn sàng**

### Event 4

Báo hỏng → Trạng thái **Đang sửa**

### Event 5

Thanh lý → Không cho phép tiếp tục sử dụng

------------------------------------------------------------------------

# 7. Giao diện

-   Dashboard
-   Danh sách tài sản
-   Form tài sản
-   Danh mục
-   Phòng họp
-   Đặt phòng
-   Lịch sử sử dụng

------------------------------------------------------------------------

# 8. Biểu đồ minh họa (ví dụ)

``` text
Tài sản theo trạng thái

██████████████  Sẵn sàng
███████         Đang dùng
███             Đang sửa
█               Thanh lý
```

``` text
Số lượt đặt phòng

T1 ████
T2 ██████
T3 █████
T4 ████████
T5 █████████
T6 ██████
```

------------------------------------------------------------------------

# 9. Kết quả đạt được

-   Hoàn thành module Odoo
-   CRUD tài sản
-   CRUD phòng họp
-   CRUD booking
-   Quản lý lịch sử
-   Phân loại tài sản
-   Dữ liệu demo
-   Giao diện tiếng Việt
-   PostgreSQL
-   Odoo ORM
-   Validation dữ liệu
-   Tự động hóa quy trình

------------------------------------------------------------------------

# 10. Hướng phát triển

-   Dashboard KPI
-   Graph View
-   Pivot View
-   Calendar
-   Kanban
-   QR Code
-   Barcode
-   Email
-   Import Excel
-   Export Excel
-   REST API
-   Mobile App

------------------------------------------------------------------------

# 11. Hướng dẫn chạy

``` bash
source venv/bin/activate
python3 odoo-bin -c odoo.conf
```

Database:

    odoo_training

Module:

    asset_management

------------------------------------------------------------------------

# Công nghệ

-   Odoo 15
-   Python
-   PostgreSQL
-   XML
-   ORM
-   Git

------------------------------------------------------------------------

# Tác giả

**Hoàng Trung Hải**

Enterprise Software Management Project
