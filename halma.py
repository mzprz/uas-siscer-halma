# -*- coding: utf-8 -*-
"""
Program utama, bekerja sebagai controller

@author: Mursito
"""

from halma_model import HalmaModel
from halma_view import HalmaView
from halma_player import HalmaPlayer
from halma_player_02_A import HalmaPlayer02 as pr
from halma_player_pr2 import HalmaPlayer02 as pr2
from halma_player_pr3 import HalmaPlayer02 as pr3

model = HalmaModel()
layar = HalmaView()

def halma(p1, p2):
    valid = model.S_OK
    model.awal(p1, p2)
    layar.tampilAwal(model)
    while (valid==model.S_OK):
        model.mainMulai()
        layar.tampilMulai(model)
        g = model.getGiliran()
        p = model.getPemain(g)
        tujuan, asal, aksi = p.main(model)
        selesai = model.getWaktu()
        if (aksi == model.A_LONCAT):
            for xy in tujuan:
                valid = model.mainLoncat(asal[0], asal[1], xy[0], xy[1])
                if (valid == model.S_OK):
                    layar.tampilLoncat(model, asal[0], asal[1], xy[0], xy[1])
                    asal = xy # usulan solusi BUG#1
        elif (aksi == model.A_GESER):
            valid = model.mainGeser(asal[0], asal[1], tujuan[0][0], tujuan[0][1])
            if (valid == model.S_OK):
                layar.tampilGeser(model, asal[0], asal[1], tujuan[0][0], tujuan[0][1])
        else:
            layar.tampilHenti(model)
        if model.akhir():
            break
        valid = model.ganti(selesai)
        if valid:
            layar.tampilGanti(model)
    layar.tampilAkhir(model, valid)


p1=pr("P1")
p2=pr("P2")

halma(p1, p2)
