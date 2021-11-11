SELECT 
	ln.div_name 
	, r.div
	, l AS unique_season
	, r.row_number
	, r.hometeam 
	, r.awayteam
	, r.hometeam_instance 
	, r.awayteam_instance 
	, r.hghg AS hthg 
	, r.htag AS htag 
	, r.ht_total_goals 
	, r.fthg 
	, r.ftag 
	, r.ft_total_goals 
	, r.h_scored AS avg_h_scored
	, r.a_conc AS avg_a_conc
	, r.a_scored AS avg_a_scored
	, r.h_conc AS avg_h_conc
	, r.h_form_over25 
	, r.h_form_under25 
	, r.a_form_over25 
	, r.a_form_under25 

FROM 
	public.tbl_backtest AS r 
	LEFT JOIN public.tbl_league_names AS ln 
		ON r.div = ln.div 
WHERE 
	r.date < ln.start_17_18 
ORDER BY 
	div_name ASC 
	, unique_season ASC 
	, hometeam_instance ASC


