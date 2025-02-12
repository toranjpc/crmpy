function toShamsi(gtime) {
	gd = parseInt(gtime[2]);
	gm = parseInt(gtime[1]);
	gy = parseInt(gtime[0]);
	var g_d_m, jy, jm, jd, gy2, days;
	g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
	gy2 = (gm > 2) ? (gy + 1) : gy;
	days = 355666 + (365 * gy) + ~~((gy2 + 3) / 4) - ~~((gy2 + 99) / 100) + ~~((gy2 + 399) / 400) + gd + g_d_m[gm - 1];
	jy = -1595 + (33 * ~~(days / 12053));
	days %= 12053;
	jy += 4 * ~~(days / 1461);
	days %= 1461;
	if (days > 365) {
		jy += ~~((days - 1) / 365);
		days = (days - 1) % 365;
	}
	if (days < 186) {
		jm = 1 + ~~(days / 31);
		jd = 1 + (days % 31);
	} else {
		jm = 7 + ~~((days - 186) / 30);
		jd = 1 + ((days - 186) % 30);
	}
	return [jd, jm, jy];
}
function toMiladi(jtime) {
	jd = parseInt(jtime[0]);
	jm = parseInt(jtime[1]);
	jy = parseInt(jtime[2]);
	var sal_a, gy, gm, gd, days;
	jy += 1595;
	days = -355668 + (365 * jy) + (~~(jy / 33) * 8) + ~~(((jy % 33) + 3) / 4) + jd + ((jm < 7) ? (jm - 1) * 31 : ((jm - 7) * 30) + 186);
	gy = 400 * ~~(days / 146097);
	days %= 146097;
	if (days > 36524) {
		gy += 100 * ~~(--days / 36524);
		days %= 36524;
		if (days >= 365) days++;
	}
	gy += 4 * ~~(days / 1461);
	days %= 1461;
	if (days > 365) {
		gy += ~~((days - 1) / 365);
		days = (days - 1) % 365;
	}
	gd = days + 1;
	sal_a = [0, 31, ((gy % 4 === 0 && gy % 100 !== 0) || (gy % 400 === 0)) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	for (gm = 0; gm < 13 && gd > sal_a[gm]; gm++) gd -= sal_a[gm];
	return [gy, gm, gd];
}
function diffInDays(s_date, e_date) {
	if (!s_date || !e_date || s_date.length != 3 || e_date.length != 3) return 0;

	sdate = new Date(s_date[0], s_date[1] - 1, s_date[2]);
	edate = new Date(e_date[0], e_date[1] - 1, e_date[2]);
	return Math.round((edate - sdate) / (1000 * 60 * 60 * 24));
}
// // console.log(toShamsi([8, 9, 2022])); //["17", "06", "1401"]
// // console.log(toMiladi(["17", "06", "1401"])); //[8, 9, 2022]
// // console.log(diffInDays([8, 9, 2022],[19, 9, 2022])); //10