def doi_tien(so_tien_muon_doi):
    menh_gia = [500000, 200000, 100000, 50000]
    so_to = {}

    for gia_tri in menh_gia:
        so_to[gia_tri] = so_tien_muon_doi // gia_tri
        so_tien_muon_doi %= gia_tri

    return so_to, so_tien_muon_doi
so_tien_muon_doi = 1375000
so_to, tien_con_lai = doi_tien(so_tien_muon_doi)
print(f"Số tờ 500000: {so_to[500000]}")
print(f"Số tờ 200000: {so_to[200000]}")
print(f"Số tờ 100000: {so_to[100000]}")
print(f"Số tờ 50000: {so_to[50000]}")
print(f"Tiền còn lại: {tien_con_lai}")
