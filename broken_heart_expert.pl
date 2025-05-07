:- dynamic gejala/1.

% Aturan diagnosa berdasarkan kombinasi gejala

diagnosa("Overthinking Syndrome") :-
    gejala(terlalu_banyak_mikir),
    gejala(mikirin_dia_setiap_malam),
    gejala(sulit_tidur).

diagnosa("Stuck in The Past Disorder") :-
    gejala(flashback_tiba_tiba),
    gejala(susah_move_on),
    gejala(berharap_balikan).

diagnosa("Ghosted Trauma") :-
    gejala(menunggu_chat),
    gejala(merasa_dibohongi),
    gejala(kosong).

diagnosa("Friendzone Flu") :-
    gejala(curhat_terus),
    gejala(berharap_balikan),
    gejala(kehilangan_minat).

diagnosa("Unrequited Love Condition") :-
    gejala(berharap_balikan),
    gejala(mikirin_dia_setiap_malam),
    gejala(kosong).

diagnosa("Clingy Attachment Syndrome") :-
    gejala(emosional),
    gejala(takut_disakiti_lagi),
    gejala(susah_move_on).

diagnosa("Jealousy Fever") :-
    gejala(stalking_pacar_baru),
    gejala(stalking_media_sosial),
    gejala(terlalu_banyak_mikir).

diagnosa("Validation Dependency Disorder") :-
    gejala(curhat_terus),
    gejala(emosional),
    gejala(kehilangan_minat).

diagnosa("Trust Collapse") :-
    gejala(merasa_dibohongi),
    gejala(takut_disakiti_lagi),
    gejala(kosong).
