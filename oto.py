# phân tích bộ dữ liệu về oto trên thế giới
import csv
import random
import pandas as pd
import statistics
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
import scipy.stats as stats
# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('oto.csv')
print("in bảng dữ liệu ra màn hình",df)
first_10_rows=df[:10]
# Chọn cột dữ liệu bạn muốn tạo bảng tần số
count= 'Vehicle Primary Use'
count1= 'Battery Electric Vehicles (BEVs)'
# Tạo bảng tần số
frequencies = df[count].value_counts()
frequencies1= df[count1].value_counts()
plt.pie(frequencies,autopct="%1.1f%%")
plt.title('biểu đồ tròn về xe')
plt.show()

# In bảng tần số
print('in bảng tần số',frequencies)
# Đọc dữ liệu từ tệp CSV
data = []
with open('oto.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# Khởi tạo biến để lưu trữ thành phố có lượng xe cao nhất
thanh_pho= None
xe_lon_nhat= 0

# Duyệt qua dữ liệu
for row in data:
    # Chuyển đổi giá trị "Vehicle Pri" sang số
    try:
        xe = int(row['Battery Electric Vehicles (BEVs)'])
    except ValueError:
        # Bỏ qua hàng nếu giá trị không thể chuyển đổi sang số
        continue

    # Cập nhật thành phố và số lượng xe  cao nhất
    if xe > xe_lon_nhat:
        thanh_pho = row['County']
        xe_lon_nhat = xe

# In kết quả
print(f"Thành phố có lượng xe điện nhiều nhất: {thanh_pho}")
print(f"Số lượng xe : {xe_lon_nhat}")

# Khởi tạo biến để lưu trữ thành phố có lượng xe cao nhất
thanh_pho1= None
xe_lon_nhat1= 0

# Duyệt qua dữ liệu
for row in data:
    # Chuyển đổi giá trị "Vehicle Pri" sang số
    try:
        xe1 = int(row['Plug-In Hybrid Electric Vehicles (PHEVs)'])
    except ValueError:
        # Bỏ qua hàng nếu giá trị không thể chuyển đổi sang số
        continue

    # Cập nhật thành phố và số lượng xe  cao nhất
    if xe1 > xe_lon_nhat1:
        thanh_pho1 = row['County']
        xe_lon_nhat1 = xe1

# In kết quả
print(f"Thành phố có lượng xe hybrid nhiều nhất: {thanh_pho1}")
print(f"Số lượng xe : {xe_lon_nhat1}")

hat= 'State'
tanso= df[hat].value_counts()
print('số lượng quận của các tiểu bang',tanso)
states = ["WA", "CA", "VA", "FL", "TX", "OR", "MD", "NC", "GA", "NJ"]
counties = [315, 95, 66, 53, 45, 34, 28, 27, 27, 21]
import matplotlib.pyplot as plt

# Tạo biểu đồ
plt.figure(figsize=(10, 6))  # Cài đặt kích thước biểu đồ
plt.bar(states, counties, color='skyblue')  # Vẽ biểu đồ cột

# Thêm tiêu đề và nhãn
plt.title("Số lượng quận theo 10 tiểu bang")
plt.xlabel("Tiểu bang")
plt.ylabel("Số lượng quận")

# Hiển thị biểu đồ
plt.xticks(rotation=0)  # Xoay nhãn x để dễ đọc hơn
plt.tight_layout()  # Tự động điều chỉnh khoảng cách giữa các thành phần
plt.show()

#xem thông tin của dataFrame
print('hiển thị thông tin dataframe')
df.info()
#hiển thị 10 dong dầu tiên
print('hiển thị 10 dong đầu tiên',df.head(10))
print("thống kê tóm tắt")
print (df.describe())
data = df['Percent Electric Vehicles']
Sai_so = sem(data)
print("Sai số tiêu chuẩn của cột là: " ,Sai_so)
data = df['Percent Electric Vehicles']
result = scipy.stats.describe (data, ddof=1, bias=False)
print('in ra phạm vi cột dữ liệu',result)
print("Lọc dữ liệu rác")
print(df.isna().sum(axis=1))
# Lấy số dòng số cột
print('số dòng và cột là ',df.shape)
#lấy mẫu ngẫu nhiên từ hai cột dữ liệu vehicle primary use và total vehicle
np.random.seed(0)
#create DataFrame
df2 = pd.DataFrame({'Vehicle Primary Use': np.repeat(np.arange(1,11), 20),
'Total Vehicles': np.random.normal(loc=7,
scale=1, size=200)})
print ("in data frame ")
print (df2)
# Thống kê số lần xuất hiện của mỗi ngày
day_counts = df['Date'].value_counts()
print (day_counts)
# kiểm định t-test hai mẫu so sánh số lượng xe điện và xe hybrid được đăng kí giữa hai tiểu bang
# Đọc dữ liệu từ file CSV
df = pd.read_csv('oto.csv')

# Tách dữ liệu theo tiểu bang
ca_data = df[df['State'] == 'California']
va_data = df[df['State'] == 'Virginia']

# Trích xuất số lượng xe điện và xe hybrid cắm điện
ca_electric = ca_data['Battery Electric Vehicles (BEVs)']
ca_hybrid = ca_data['Plug-In Hybrid Electric Vehicles (PHEVs)']

va_electric = va_data['Battery Electric Vehicles (BEVs)']
va_hybrid = va_data['Plug-In Hybrid Electric Vehicles (PHEVs)']

# Kết hợp dữ liệu thành hai mảng
ca_data = pd.concat([ca_electric, ca_hybrid], axis=1).mean()
va_data = pd.concat([va_electric, va_hybrid], axis=1).mean()

# Thực hiện kiểm định t-test hai mẫu
t_statistic, p_value = stats.ttest_ind(ca_data, va_data)

# In kết quả
print(f"Thống kê t: {t_statistic:.2f}")
print(f"Giá trị p: {p_value:.4f}")

# Kiểm tra kết quả
alpha = 0.05  # Trình độ tin cậy (ví dụ: 95%)

if p_value < alpha:
    print(f"Bác bỏ giả thuyết H0 - Số lượng xe điện và xe hybrid cắm điện được đăng ký trung bình giữa hai tiểu bang California và Virginia khác biệt nhau (mức tin cậy {alpha*100:.2f}%)")
else:
    print(f"Không thể bác bỏ giả thuyết H0 - Dữ liệu không đủ để kết luận chắc chắn (mức tin cậy {alpha*100:.2f}%)")


#kiểm định t-test một mẫu so sánh số lượng xe điện và hybrid đăng kí của tiểu bang caliifonia và vỉginia
# Lọc dữ liệu tháng 1
jan_data = df[df['Date'] == 'January']

# Tách dữ liệu theo tiểu bang
ca_data = jan_data[df['State'] == 'California']
va_data = jan_data[df['State'] == 'Virginia']

# Trích xuất số lượng xe điện và xe hybrid cắm điện
ca_electric = ca_data['Battery Electric Vehicles (BEVs)']
ca_hybrid = ca_data['Plug-In Hybrid Electric Vehicles (PHEVs)']

va_electric = va_data['Battery Electric Vehicles (BEVs)']
va_hybrid = va_data['Plug-In Hybrid Electric Vehicles (PHEVs)']

# Kết hợp dữ liệu thành hai mảng
ca_data = pd.concat([ca_electric, ca_hybrid], axis=1).mean()
va_data = pd.concat([va_electric, va_hybrid], axis=1).mean()

# Giả sử giá trị trung bình giả định (ví dụ: trung bình toàn quốc) là 1000
mean = 1000

# Thực hiện kiểm định t-test một mẫu cho mỗi tiểu bang
t_statistic_ca, p_value_ca = stats.ttest_1samp(ca_data, mean)
t_statistic_va, p_value_va = stats.ttest_1samp(va_data, mean)

# In kết quả
print("Kết quả kiểm định t-test cho California:")
print(f"Thống kê t: {t_statistic_ca:.2f}")
print(f"Giá trị p: {p_value_ca:.4f}")

print("Kết quả kiểm định t-test cho Virginia:")
print(f"Thống kê t: {t_statistic_va:.2f}")
print(f"Giá trị p: {p_value_va:.4f}")

# Kiểm tra kết quả
alpha = 0.05  # Trình độ tin cậy (ví dụ: 95%)

# California
if p_value_ca < alpha:
    print(f"\tCalifornia: Bác bỏ giả thuyết H0 - Số lượng xe điện và xe hybrid cắm điện được đăng ký trung bình trong tháng 1 khác biệt so với {mean} (mức tin cậy {alpha*100:.2f}%)")
else:
    print(f"\tCalifornia: Không thể bác bỏ giả thuyết H0 - Dữ liệu không đủ để kết luận chắc chắn (mức tin cậy {alpha*100:.2f}%)")

# Virginia
if p_value_va < alpha:
    print(f"\tVirginia: Bác bỏ giả thuyết H0 - Số lượng xe điện và xe hybrid cắm điện được đăng ký trung bình trong tháng 1 khác biệt so với {mean} (mức tin cậy {alpha*100:.2f}%)")
else:
    print(f"\tVirginia: Không thể bác bỏ giả thuyết H0 - Dữ liệu không đủ để kết luận chắc chắn (mức tin cậy {alpha*100:.2f}%)")
