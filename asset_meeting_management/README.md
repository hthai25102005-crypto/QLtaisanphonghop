# Asset & Meeting Room Management System (Odoo 15)

## 📌 Giới thiệu
Hệ thống quản lý tài sản và phòng họp tích hợp HRM được xây dựng trên Odoo 15.

Module cho phép:
- Quản lý tài sản doanh nghiệp
- Quản lý phòng họp
- Đặt lịch họp
- Phân bổ tài sản cho cuộc họp
- Theo dõi lịch sử sử dụng
- Tự động cập nhật trạng thái tài sản & phòng họp

---

## 📌 Công nghệ sử dụng
- Python 3
- Odoo 15
- PostgreSQL
- XML (UI Views)
- ORM Odoo

---

## 📌 Module tích hợp
- HR Module (hr.employee)
- Mail Thread (chatter)
- Calendar integration (logic booking)

---

## 📌 Chức năng chính

### 1. Quản lý tài sản
- Laptop, máy chiếu, TV, camera...
- Theo dõi trạng thái:
  Available / Reserved / In Use / Maintenance

### 2. Quản lý phòng họp
- Tạo phòng họp
- Sức chứa
- Trạng thái phòng

### 3. Đặt lịch họp
- Nhân viên tạo booking
- Chọn phòng + thời gian
- Kiểm tra trùng lịch

### 4. Gán tài sản cho cuộc họp
- Máy chiếu, laptop, thiết bị hỗ trợ

### 5. Tự động hóa
- Khi booking được duyệt:
  - Phòng chuyển sang BOOKED
  - Tài sản chuyển sang RESERVED
- Khi kết thúc:
  - Trạng thái reset về AVAILABLE

---

## 📌 Business Flow (tóm tắt)

Nhân viên → tạo booking → chọn phòng → chọn tài sản → quản lý duyệt → hệ thống tự cập nhật trạng thái → hoàn tất cuộc họp

---

## 📌 Cấu trúc module

asset_meeting_management/
├── models/
├── views/
├── security/
├── data/
├── wizard/
├── report/

---

## 📌 Yêu cầu chạy

```bash
# copy module vào addons
cp -r asset_meeting_management custom_addons/

# update apps
odoo -u asset_meeting_management

