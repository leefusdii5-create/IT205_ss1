# Phân tích và Đề xuất giải pháp
# Input: kiểu dữ liệu ban đầu là string
# Output: kiểu dữ liệu mong muốn của đầu ra là
# str: mã bệnh nhân
# float: nhiệt độ cơ thể
# int: nhịp tim

# 2 giải pháp để ép kiểu dữ liệu
# Giải pháp 1: Ép kiểu trực tiếp khi nhập dữ liệu
# vd: score = int(input("Nhap diem: "))
# Giải pháp 2: Nhập chuỗi trước rồi ép kiểu sau
# vd: score_input = input("Nhap diem: ")
# score = int(score_input)

# So sánh
#                           Giải pháp 1                          Giải pháp 2
# Số lượng biến               Ít hơn                              Nhiều hơn
# Độ ngắn gọn code            Ngắn gọn                            Dài hơn
# Tiết kiệm bộ nhớ            Tốt hơn                             Tốn hơn
# Dễ debug                    Khó hơn                             Dễ hơn
# Kiểm tra dữ liệu gốc          Khó                                 Dễ
# Phù hợp hệ thống lớn        Trung bình                           Tốt

# Chốt lựa chọn: Giải pháp 2 phù hợp nhất trong môi trường bệnh viện vì dễ kiểm tra, dễ dò lỗi và đảm bảo độ an toàn dữ liệu cao hơn

# Triển khai code
print("===== HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN =====")
patient_id = input("Nhập mã bệnh nhân: ")
temp_input = input("Nhập nhiệt độ cơ thể: ")
heart_input = input("Nhập nhịp tim: ")

temperature = float(temp_input)
heart_rate = int(heart_input)

print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", patient_id)
print("Nhiệt độ cơ thể:", temperature, "độ C")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))
print("Nhịp tim:", heart_rate, "nhịp/phút")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))
print("\nThông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")
