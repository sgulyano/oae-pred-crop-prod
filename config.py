from utils.preprocess import rice_inseason_harvest_season, rice_offseason_harvest_season, corn_harvest_season, cassava_harvest_season, rubber_harvest_season

params = {
    'rice_in-season': {
        'yield_file' : 'Clean13products/_01.ข้าวนาปี/ปริมาณผลผลิตข้าวนาปี_2545-61.xlsx',
        'cost_file' : ['Clean13products/_01.ข้าวนาปี/1) ข้าวนาปี1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_01.ข้าวนาปี/1) ข้าวนาปี2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_01.ข้าวนาปี/1) ข้าวนาปี3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_01.ข้าวนาปี/1) ข้าวนาปี5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_01.ข้าวนาปี/ราคาข้าวเปลือกเจ้านาปี ความชื้น 15_._clean.xls'],
        'col_price'  : ['price'],
        'harvest' : rice_inseason_harvest_season,
        'seasonality_prior_scale': 0.1,
        'fourier_order': 7,
        'prior_scale': 0.1
    },
    
    'rubber': {
        'yield_file' : 'Clean13products/_01.ยางพารา/ปริมาณผลผลิตยางพารา_2548-60.xlsx',
        'cost_file' : ['Clean13products/_01.ยางพารา/19) ยางพารา1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_01.ยางพารา/19) ยางพารา2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_01.ยางพารา/19) ยางพารา3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_01.ยางพารา/19) ยางพารา5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_01.ยางพารา/ราคาน้ำยางสดคละ._clean.xls',
                        'Clean13products/_01.ยางพารา/ราคายางก้อน._clean.xls',
                        'Clean13products/_01.ยางพารา/ราคายางแผ่นดิบชั้น3._clean.xls'],
        'col_price'  : ['price_latex', 'price_cup', 'price_sheet'],
        'harvest' : rubber_harvest_season,
        'seasonality_prior_scale': 1,
        'fourier_order': 3,
        'prior_scale': 5
    },
    
    'rice_off-season': {
        'yield_file' : 'Clean13products/_02.ข้าวนาปรัง/ปริมาณผลผลิตข้าวนาปรัง_2536-62.xlsx',
        'cost_file' : ['Clean13products/_02.ข้าวนาปรัง/7) ข้าวนาปรัง1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_02.ข้าวนาปรัง/7) ข้าวนาปรัง2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_02.ข้าวนาปรัง/7) ข้าวนาปรัง3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_02.ข้าวนาปรัง/7) ข้าวนาปรัง5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_02.ข้าวนาปรัง/ราคาข้าวเปลือกเจ้านาปรัง ความชื้น15_._clean.xls'],
        'col_price'  : ['price'],
        'harvest' : rice_offseason_harvest_season,
        'seasonality_prior_scale': 0.1,
        'fourier_order': 5,
        'prior_scale': 0.1
    },
    
    'palm': {
        'yield_file' : 'Clean13products/_02.ปาล์มน้ำมัน/ปริมาณผลผลิตปาล์มน้ำมัน_2525-61.xlsx',
        'cost_file' : ['Clean13products/_02.ปาล์มน้ำมัน/18) ปาล์มน้ำมัน1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_02.ปาล์มน้ำมัน/18) ปาล์มน้ำมัน2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_02.ปาล์มน้ำมัน/18) ปาล์มน้ำมัน3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_02.ปาล์มน้ำมัน/18) ปาล์มน้ำมัน5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_02.ปาล์มน้ำมัน/ราคาปาล์มน้ำมันทั้งทะลาย นน.มากกว่า 15 กก.._clean.xls',
                        'Clean13products/_02.ปาล์มน้ำมัน/ราคาปาล์มน้ำมันร่วง._clean.xls'],
        'col_price'  : ['price1', 'price2'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'coffee': {
        'yield_file' : 'Clean13products/_03.กาแฟ/ปริมาณผลผลิตกาแฟ_2526-63.xlsx',
        'cost_file' : ['Clean13products/_03.กาแฟ/20) กาแฟ1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_03.กาแฟ/20) กาแฟ2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_03.กาแฟ/20) กาแฟ3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_03.กาแฟ/20) กาแฟ5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_03.กาแฟ/ราคาผลกาแฟ(อราบิก้า)สดคละ._clean.xls',
                        'Clean13products/_03.กาแฟ/ราคาสารกาแฟ(โรบัสต้า)คละ._clean.xls',
                        'Clean13products/_03.กาแฟ/ราคาสารกาแฟ(อราบิก้า)คละ._clean.xls'],
        'col_price'  : ['price_arabica1', 'price_robusta', 'price_arabica2'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'corn': {
        'yield_file' : 'Clean13products/_03.ข้าวโพดเลี้ยงสัตว์/ปริมาณผลผลิตข้าวโพดเลี้ยงสัตว์_รวมรุ่น_2539-61.xlsx',
        'cost_file' : ['Clean13products/_03.ข้าวโพดเลี้ยงสัตว์/8) ข้าวโพดเลี้ยงสัตว์1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_03.ข้าวโพดเลี้ยงสัตว์/8) ข้าวโพดเลี้ยงสัตว์2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_03.ข้าวโพดเลี้ยงสัตว์/8) ข้าวโพดเลี้ยงสัตว์3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_03.ข้าวโพดเลี้ยงสัตว์/8) ข้าวโพดเลี้ยงสัตว์5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_03.ข้าวโพดเลี้ยงสัตว์/ราคาข้าวโพดเลี้ยงสัตว์ความชื้น14.5_._clean.xls',
                        'Clean13products/_03.ข้าวโพดเลี้ยงสัตว์/ราคาข้าวโพดเลี้ยงสัตว์ความชื้นเกิน14.5_._clean.xls'],
        'col_price'  : ['price1', 'price2'],
        'harvest' : corn_harvest_season,
        'seasonality_prior_scale': 0.1,
        'fourier_order': 3,
        'prior_scale': 0.1
    },
    
    'cassava': {
        'yield_file' : 'Clean13products/_04.มันสำปะหลัง/ปริมาณผลผลิตมันสำปะหลัง_2545-62.xlsx',
        'cost_file' : ['Clean13products/_04.มันสำปะหลัง/9) มันสำปะหลัง1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_04.มันสำปะหลัง/9) มันสำปะหลัง2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_04.มันสำปะหลัง/9) มันสำปะหลัง3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_04.มันสำปะหลัง/9) มันสำปะหลัง5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_04.มันสำปะหลัง/ราคาหัวมันสำปะหลัง (แป้ง 25_)._clean.xls',
                        'Clean13products/_04.มันสำปะหลัง/ราคาหัวมันสำปะหลังสดคละ._clean.xls'],
        'col_price'  : ['price1', 'price2'],
        'harvest' : cassava_harvest_season,
        'seasonality_prior_scale': 0.1,
        'fourier_order': 3,
        'prior_scale': 0.1
    },
    
    'longan': {
        'yield_file' : 'Clean13products/_04.ลำไย/ปริมาณผลผลิตลำไย_2549-62.xlsx',
        'cost_file' : ['Clean13products/_04.ลำไย/22) ลำไย1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_04.ลำไย/22) ลำไย2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_04.ลำไย/22) ลำไย3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_04.ลำไย/22) ลำไย5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_04.ลำไย/ราคาลำไยเกรด  AA._clean.xls',
                        'Clean13products/_04.ลำไย/ราคาลำไยเกรด  A._clean.xls',
                        'Clean13products/_04.ลำไย/ราคาลำไยคละ._clean.xls'],
        'col_price'  : ['price_AA', 'price_A', 'price1'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'durian': {
        'yield_file' : 'Clean13products/_05.ทุเรียน/ปริมาณผลผลิตทุเรียน_2540-62.xlsx',
        'cost_file' : ['Clean13products/_05.ทุเรียน/26) ทุเรียน1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_05.ทุเรียน/26) ทุเรียน2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_05.ทุเรียน/26) ทุเรียน3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_05.ทุเรียน/26) ทุเรียน5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_05.ทุเรียน/ราคาทุเรียนชะนี._clean.xls',
                        'Clean13products/_05.ทุเรียน/ราคาทุเรียนหมอนทอง._clean.xls'],
        'col_price'  : ['price1', 'price2'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'pineapple': {
        'yield_file' : 'Clean13products/_05.สับปะรด/ปริมาณผลผลิตสับปะรด_2538-61.xlsx',
        'cost_file' : ['Clean13products/_05.สับปะรด/13) สับปะรด1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_05.สับปะรด/13) สับปะรด2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_05.สับปะรด/13) สับปะรด3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_05.สับปะรด/13) สับปะรด5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_05.สับปะรด/ราคาสับปะรดบริโภค._clean.xls',
                        'Clean13products/_05.สับปะรด/ราคาสับปะรดโรงงาน._clean.xls'],
        'col_price'  : ['price1', 'price2'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'rambutan': {
        'yield_file' : 'Clean13products/_06.เงาะ/ปริมาณผลผลิตเงาะ_2540-62.xlsx',
        'cost_file' : ['Clean13products/_06.เงาะ/24) เงาะ1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_06.เงาะ/24) เงาะ2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_06.เงาะ/24) เงาะ3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_06.เงาะ/24) เงาะ5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_06.เงาะ/ราคาเงาะโรงเรียนคละ._clean.xls'],
        'col_price'  : ['price'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'mangosteen': {
        'yield_file' : 'Clean13products/_07.มังคุด/ปริมาณผลผลิตมังคุด_2525-62.xlsx',
        'cost_file' : ['Clean13products/_07.มังคุด/25) มังคุด1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_07.มังคุด/25) มังคุด2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_07.มังคุด/25) มังคุด3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_07.มังคุด/25) มังคุด5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_07.มังคุด/ราคามังคุดผิวมันผลขนาดใหญ่._clean.xls',
                        'Clean13products/_07.มังคุด/ราคามังคุดผิวมันผลขนาดกลาง._clean.xls',
                        'Clean13products/_07.มังคุด/ราคามังคุดผิวมันผลขนาดคละ._clean.xls',
                        'Clean13products/_07.มังคุด/ราคามังคุดคละ._clean.xls'],
        'col_price'  : ['price1', 'price2', 'price3', 'price4'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'cane': {
        'yield_file' : 'Clean13products/_07.อ้อยโรงงาน/ปริมาณผลผลิตอ้อยโรงงาน_2532-57.xlsx',
        'cost_file' : [],
        'price_file' : ['Clean13products/_07.อ้อยโรงงาน/ราคาอ้อยโรงงาน._clean.xls'],
        'col_price'  : ['price'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    },
    
    'coconut': {
        'yield_file' : 'Clean13products/_11.มะพร้าว/ปริมาณผลผลิตมะพร้าวแก่_2537-62.xlsx',
        'cost_file' : ['Clean13products/_11.มะพร้าว/28) มะพร้าว1.ต้นทุนผันแปร_clean.xls', 
                       'Clean13products/_11.มะพร้าว/28) มะพร้าว2.ต้นทุนคงที่_clean.xls',
                       'Clean13products/_11.มะพร้าว/28) มะพร้าว3.ต้นทุนรวมต่อไร่_clean.xls',
                       'Clean13products/_11.มะพร้าว/28) มะพร้าว5.ผลตอบแทนสุทธิต่อไร่_clean.xls'],
        'price_file' : ['Clean13products/_11.มะพร้าว/ราคามะพร้าวผลแห้งคละ._clean.xls',
                        'Clean13products/_11.มะพร้าว/ราคามะพร้าวผลแห้งใหญ่._clean.xls'],
        'col_price'  : ['price1', 'price2'],
        'harvest' : None,
        'seasonality_prior_scale': 10,
        'prior_scale': 0.1
    }
}