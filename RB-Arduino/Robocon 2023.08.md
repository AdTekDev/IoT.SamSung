# Robo Car



## PS2:
	1. lib - http://www.billporter.info/2010/06/05/playstation-2-controller-arduino-library-v1-0/  
	2. guide - http://www.nguyenvankhoa.com/2020/01/huong-dan-cach-lap-trinh-arduino-uno-r3.html  
	3. video - https://www.youtube.com/watch?v=8WgGhXb3A18    
	4. lib 2 - https://github.com/madsci1016/Arduino-PS2X  
	5. Chân đế:  
		GND <-> GND  
		SS <-> D10  
		CLK <-> D13  
		MISO <-> D12  
		MOSI <-> D11  
		5V <-> 5V  
	6. Code 2 - https://nshopvn.com/product/remote-dieu-khien-ps2-khong-day-ps2-robot-controller/  
	

	
	
## Động Cơ DC Servo JGB37-520:
	1. Thiết bị - https://hshop.vn/products/bo-dong-co-dc-servo-jgb37-520-kem-ga-bat-va-banh-xe-v2-65mm  
	2. Chân:  
		M1 : Dây cấp nguồn cho động cơ.   
		GND : Dây cấp nguồn cho Encoder, 0VDC.  
		C1/A: Kênh trả xung A  
		C2/B: Kênh trả xung B  
		VCC: Dây cấp nguồn cho Encoder 3.3~5VDC  
		M2: Dây cấp nguồn cho động cơ  
	
	
## Điều Khiển Động Cơ DC BTS7960 43A:
	1. Thiết bị:  
	https://hshop.vn/products/mach-dieu-khien-dong-co-dc-bts796043a-1-dong-co  
	
	https://nshopvn.com/product/mach-dieu-khien-dong-co-dc-bts7960-43a-1-dong-co/  
	
	
	2. Chân:  
		VCC : Nguồn tạo mức logic điều khiển (3.3~5VDC)  
		GND : Chân đất.  
		R_EN = 0 Disable nửa cầu H phải. R_EN = 1 : Enable nửa cầu H phải.  
		L_EN  = 0 Disable nửa cầu H trái. L_EN = 1 : Enable nửa cầu H trái.  
		RPWM và LPWM : chân điều khiển đảo chiều và tốc độ động cơ.  
		RPWM = 1 và LPWM = 0 : Mô tơ quay thuận.  
		RPWM = 0 và LPWM = 1 : Mô tơ quay  nghịch  
		RPWM = 1 và LPWM = 1 hoặc RPWM = 0 và LPWM = 0 : Dừng.  
		R_IS và L_IS : kết hợp với điện trở để giới hạn dòng qua cầu H  
		​Với ứng dụng bình thường RPWM,LPWM nối với GPIO (VD : chân digital 2,3) để điều khiển chiều quay của động cơ.  
		Chân R_EN , L_EN nối chung lại rồi nối với PWM (VD chân digital 5) để điều khiển tốc độ động cơ.  
	
	3. Code:  
	https://nshopvn.com/product/mach-dieu-khien-dong-co-dc-bts7960-43a-1-dong-co/ 
 
 	https://github.com/luisllamasbinaburo/Arduino-BTS7960  
	
