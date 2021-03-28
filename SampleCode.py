
def reformatDate(date):
    arr = date.split('/')
    if(len(arr) == 3):
        if len(arr[2]) < 4:
            return arr[0]+'/'+arr[1]+'/20'+arr[2]
    else:
        return "1/1/1970"
    return date

print(reformatDate("12/3/21"))
print(reformatDate("12/3/2021"))

News = ['Thời sự','Tin tức trong ngày','TuanVietNam','Thế giới','Special','POLITICS','SOCIETY','FEATURE','Video An ninh','News']
SucKhoeDoiSong = ['Sức khỏe đời sống','Sức khỏe','Đời sống','Bạn trẻ - Cuộc sống','Tuyến đầu chống dịch','Dịch viêm phổi virus corona','Ẩm thực','Du lịch']
GiaiTri = ['Giải trí','Đời sống','Showbiz','Cười 24H','Media']
KinhDoanh = ['Kinh doanh','Kinh Doanh','Thị trường - Tiêu dùng','Thị trường - tiêu dùng','BUSINESS','Bảo vệ người tiêu dùng','Hợp tác','Bất động sản','Kinh tế cho tương lai','Pháp luật']
TheThao = ['Thể thao','World Cup 2022','Bóng đá','World Cup 2018']
GiaoDuc = ['Giáo dục','Giáo dục - du học']
CongNghe = ['Công nghệ','Khoa học','Công nghệ thông tin','SCI-TECH & ENVIRONMENT','Thông tin & Truyền thông','Số hóa']
ThoiTrang = ['Thời trang','Làm đẹp','Thời trang Hi-tech']
Xe = ['Xe','Ô tô - Xe máy','Ô tô','Xe máy - Xe đạp']
def updateCategory(cate):
    if cate in News:
        return "Tin tức"
    elif cate in SucKhoeDoiSong:
        return "Sức khoẻ"
    elif cate in GiaiTri:
        return "Giải trí"
    elif cate in KinhDoanh:
        return "Kinh doanh"
    elif cate in TheThao:
        return "Thể thao"
    elif cate in GiaoDuc:
        return "Giáo dục"
    elif cate in CongNghe:
        return "Công nghệ"
    elif cate in ThoiTrang:
        return "Thời trang"
    else:
        return "Khác"