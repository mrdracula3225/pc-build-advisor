builds = {
    "Gaming": {
        "Intel": [
            # Ultra-Budget (₹10K-₹20K)
            {"max_budget": 15000, "build": {"CPU": "Intel Celeron G6900", "GPU": "Integrated UHD 710", "RAM": "8GB DDR4", "Storage": "256GB SSD", "PSU": "300W", "Cabinet": "Basic Mini Tower", "Total": 14000}},
            {"max_budget": 20000, "build": {"CPU": "Intel Pentium Gold G7400", "GPU": "Integrated UHD 710", "RAM": "8GB DDR4", "Storage": "256GB SSD", "PSU": "350W", "Cabinet": "Mini Tower", "Total": 19000}},

            # Budget (₹20K-₹40K)
            {"max_budget": 25000, "build": {"CPU": "Intel i3 12100F", "GPU": "Used GTX 1050 Ti", "RAM": "8GB DDR4", "Storage": "512GB SSD", "PSU": "450W Bronze", "Cabinet": "Budget Mid Tower", "Total": 24000}},
            {"max_budget": 35000, "build": {"CPU": "Intel i3 13100F", "GPU": "GTX 1650", "RAM": "16GB DDR4", "Storage": "512GB NVMe SSD", "PSU": "500W Bronze", "Cabinet": "Gaming Mid Tower", "Total": 34000}},

            # Mid-Range (₹40K-₹70K)
            {"max_budget": 50000, "build": {"CPU": "Intel i5 12400F", "GPU": "RTX 3050", "RAM": "16GB DDR4", "Storage": "1TB NVMe SSD", "PSU": "550W Bronze", "Cabinet": "Gaming Mid Tower", "Total": 49000}},
            {"max_budget": 65000, "build": {"CPU": "Intel i5 13400F", "GPU": "RTX 3060 Ti", "RAM": "16GB DDR4", "Storage": "1TB NVMe SSD", "PSU": "650W Bronze", "Cabinet": "RGB Mid Tower", "Total": 64000}},

            # High-End (₹70K-₹100K)
            {"max_budget": 80000, "build": {"CPU": "Intel i7 13700F", "GPU": "RTX 4060 Ti", "RAM": "32GB DDR5", "Storage": "1TB NVMe SSD", "PSU": "750W Gold", "Cabinet": "Premium RGB Tower", "Total": 79000}},
            {"max_budget": 100000, "build": {"CPU": "Intel i7 14700KF", "GPU": "RTX 4070 Super", "RAM": "32GB DDR5", "Storage": "2TB NVMe SSD", "PSU": "850W Gold", "Cabinet": "High-Airflow Tower", "Total": 98000}},
        ],
        "AMD": [
            # Ultra-Budget (₹10K-₹20K)
            {"max_budget": 15000, "build": {"CPU": "AMD Athlon 3000G", "GPU": "Integrated Vega 3", "RAM": "8GB DDR4", "Storage": "256GB SSD", "PSU": "300W", "Cabinet": "Basic Mini Tower", "Total": 14000}},
            {"max_budget": 20000, "build": {"CPU": "AMD Ryzen 3 3200G", "GPU": "Integrated Vega 8", "RAM": "8GB DDR4", "Storage": "512GB SSD", "PSU": "350W", "Cabinet": "Mini Tower", "Total": 19000}},

            # Budget (₹20K-₹40K)
            {"max_budget": 25000, "build": {"CPU": "AMD Ryzen 5 4600G", "GPU": "Integrated Vega 7", "RAM": "16GB DDR4", "Storage": "512GB SSD", "PSU": "450W Bronze", "Cabinet": "Budget Mid Tower", "Total": 24000}},
            {"max_budget": 35000, "build": {"CPU": "AMD Ryzen 5 5600", "GPU": "RX 6400", "RAM": "16GB DDR4", "Storage": "512GB NVMe SSD", "PSU": "500W Bronze", "Cabinet": "Gaming Mid Tower", "Total": 34000}},

            # Mid-Range (₹40K-₹70K)
            {"max_budget": 50000, "build": {"CPU": "AMD Ryzen 5 7600", "GPU": "RX 6600", "RAM": "16GB DDR5", "Storage": "1TB NVMe SSD", "PSU": "550W Bronze", "Cabinet": "Gaming Mid Tower", "Total": 49000}},
            {"max_budget": 65000, "build": {"CPU": "AMD Ryzen 7 7700X", "GPU": "RX 7600 XT", "RAM": "32GB DDR5", "Storage": "1TB NVMe SSD", "PSU": "650W Gold", "Cabinet": "RGB Mid Tower", "Total": 64000}},

            # High-End (₹70K-₹100K)
            {"max_budget": 80000, "build": {"CPU": "AMD Ryzen 7 7800X3D", "GPU": "RX 7700 XT", "RAM": "32GB DDR5", "Storage": "1TB NVMe SSD", "PSU": "750W Gold", "Cabinet": "Premium RGB Tower", "Total": 79000}},
            {"max_budget": 100000, "build": {"CPU": "AMD Ryzen 9 7900X", "GPU": "RX 7900 GRE", "RAM": "32GB DDR5", "Storage": "2TB NVMe SSD", "PSU": "850W Gold", "Cabinet": "High-Airflow Tower", "Total": 98000}},
        ],
    },
    "Video Editing": {
        "Intel": [
            # Budget (₹20K-₹40K)
            {"max_budget": 25000, "build": {"CPU": "Intel i3 12100", "GPU": "Integrated UHD 730", "RAM": "16GB DDR4", "Storage": "512GB SSD", "PSU": "450W", "Cabinet": "Basic Tower", "Total": 24000}},
            {"max_budget": 35000, "build": {"CPU": "Intel i5 12400", "GPU": "GTX 1650", "RAM": "16GB DDR4", "Storage": "512GB SSD + 1TB HDD", "PSU": "500W Bronze", "Cabinet": "Silent Case", "Total": 34000}},

            # Mid-Range (₹40K-₹70K)
            {"max_budget": 50000, "build": {"CPU": "Intel i5 13400", "GPU": "RTX 3050", "RAM": "32GB DDR4", "Storage": "1TB NVMe SSD", "PSU": "600W Bronze", "Cabinet": "Silent Case", "Total": 49000}},
            {"max_budget": 70000, "build": {"CPU": "Intel i7 13700", "GPU": "RTX 3060 Ti", "RAM": "32GB DDR5", "Storage": "1TB NVMe SSD + 2TB HDD", "PSU": "750W Gold", "Cabinet": "Silent Case", "Total": 69000}},

            # High-End (₹70K-₹100K)
            {"max_budget": 85000, "build": {"CPU": "Intel i7 14700K", "GPU": "RTX 4070", "RAM": "64GB DDR5", "Storage": "2TB NVMe SSD", "PSU": "850W Gold", "Cabinet": "Workstation Tower", "Total": 84000}},
            {"max_budget": 100000, "build": {"CPU": "Intel i9 14900K", "GPU": "RTX 4080", "RAM": "64GB DDR5", "Storage": "2TB NVMe SSD + 4TB HDD", "PSU": "1000W Platinum", "Cabinet": "High-Airflow Tower", "Total": 99000}},
        ],
        "AMD": [
            # Budget (₹20K-₹40K)
            {"max_budget": 25000, "build": {"CPU": "AMD Ryzen 5 5600G", "GPU": "Integrated Vega 7", "RAM": "16GB DDR4", "Storage": "512GB SSD", "PSU": "450W", "Cabinet": "Basic Tower", "Total": 24000}},
            {"max_budget": 35000, "build": {"CPU": "AMD Ryzen 5 5600", "GPU": "RX 6400", "RAM": "16GB DDR4", "Storage": "512GB SSD + 1TB HDD", "PSU": "500W Bronze", "Cabinet": "Silent Case", "Total": 34000}},

            # Mid-Range (₹40K-₹70K)
            {"max_budget": 50000, "build": {"CPU": "AMD Ryzen 7 7700", "GPU": "RX 6600", "RAM": "32GB DDR5", "Storage": "1TB NVMe SSD", "PSU": "600W Bronze", "Cabinet": "Silent Case", "Total": 49000}},
            {"max_budget": 70000, "build": {"CPU": "AMD Ryzen 9 7900", "GPU": "RX 6700 XT", "RAM": "32GB DDR5", "Storage": "1TB NVMe SSD + 2TB HDD", "PSU": "750W Gold", "Cabinet": "Silent Case", "Total": 69000}},

            # High-End (₹70K-₹100K)
            {"max_budget": 85000, "build": {"CPU": "AMD Ryzen 9 7900X", "GPU": "RX 7800 XT", "RAM": "64GB DDR5", "Storage": "2TB NVMe SSD", "PSU": "850W Gold", "Cabinet": "Workstation Tower", "Total": 84000}},
            {"max_budget": 100000, "build": {"CPU": "AMD Ryzen 9 7950X", "GPU": "RTX 4080", "RAM": "64GB DDR5", "Storage": "2TB NVMe SSD + 4TB HDD", "PSU": "1000W Platinum", "Cabinet": "High-Airflow Tower", "Total": 99000}},
        ],
    },
    "Casual Use": [
        # Ultra-Ultra-low-budget (5k)
        {"max_budget": 5000, "build": {"CPU": "Used Intel Core 2 Duo/AMD Athlon X2", "GPU": "Integrated Graphics", "RAM": "4GB DDR2/DDR3 (Used)", "Storage": "120GB Used HDD", "PSU": "Used 250W PSU", "Cabinet": "Used Mini Tower", "Total": 5000}},
        # Ultra-Budget (₹10K-₹20K)
        {"max_budget": 10000, "build": {"CPU": "Intel Celeron G6900", "GPU": "Integrated UHD 710", "RAM": "4GB DDR4", "Storage": "128GB SSD", "PSU": "300W", "Cabinet": "Basic Mini Tower", "Total": 9500}},
        {"max_budget": 15000, "build": {"CPU": "AMD Athlon 3000G", "GPU": "Integrated Vega 3", "RAM": "8GB DDR4", "Storage": "256GB SSD", "PSU": "350W", "Cabinet": "Mini Tower", "Total": 14000}},

        # Budget (₹20K-₹40K)
        {"max_budget": 25000, "build": {"CPU": "Intel i3 12100", "GPU": "Integrated UHD 730", "RAM": "8GB DDR4", "Storage": "512GB SSD", "PSU": "450W", "Cabinet": "Compact Tower", "Total": 24000}},
        {"max_budget": 35000, "build": {"CPU": "AMD Ryzen 5 5600G", "GPU": "Integrated Vega 7", "RAM": "16GB DDR4", "Storage": "512GB NVMe SSD", "PSU": "500W Bronze", "Cabinet": "Sleek Mini Tower", "Total": 34000}},

        # Premium (₹40K-₹60K)
        {"max_budget": 45000, "build": {"CPU": "Intel i5 13400", "GPU": "Integrated UHD 730", "RAM": "16GB DDR4", "Storage": "1TB NVMe SSD", "PSU": "550W Bronze", "Cabinet": "Sleek Mini Tower", "Total": 44000}},
        {"max_budget": 60000, "build": {"CPU": "AMD Ryzen 7 7700", "GPU": "Integrated RDNA 2", "RAM": "32GB DDR5", "Storage": "1TB NVMe SSD", "PSU": "600W Bronze", "Cabinet": "Premium Mini Tower", "Total": 59000}},
    ]
}