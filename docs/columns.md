# Справочник колонок

Колонки `data/accepted_2007_to_2018Q4.parquet` в порядке файла, всего: 151.

- **Описание** — из `docs/LCDataDictionary.xlsx`, лист `LoanStats`.
- **Статистика** — по всем 2,260,668 займам (без 33 служебных строк), все годы. Это технический обзор: о связи с дефолтом здесь ничего нет.
- **Пропуски, %** — доля пустых значений. **Разных ≈** — приблизительное число различных значений (DuckDB `approx_unique`, погрешность в несколько процентов: у `id` оно больше числа займов, хотя все id уникальны). **Диапазон** — минимум … максимум; для текста это алфавитный порядок, а не смысловой.

Файл сгенерирован скриптом `scripts/build_columns_md.py` — не править вручную. Как читать: Cmd + Shift + V — предпросмотр, Cmd + F — поиск по именам и описаниям.

| # | Колонка | Тип | Пропуски, % | Разных ≈ | Диапазон | Описание |
|---|---|---|---|---|---|---|
| 0 | `id` | VARCHAR | 0.0 | 2,450,049 | 1000007 … 999989 | A unique LC assigned ID for the loan listing. |
| 1 | `member_id` | VARCHAR | 100.0 | 0 |  | A unique LC assigned Id for the borrower member. |
| 2 | `loan_amnt` | DOUBLE | 0.0 | 1,432 | 500.0 … 40000.0 | The listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value. |
| 3 | `funded_amnt` | DOUBLE | 0.0 | 1,432 | 500.0 … 40000.0 | The total amount committed to that loan at that point in time. |
| 4 | `funded_amnt_inv` | DOUBLE | 0.0 | 12,255 | 0.0 … 40000.0 | The total amount committed by investors for that loan at that point in time. |
| 5 | `term` | VARCHAR | 0.0 | 2 |  36 months …  60 months | The number of payments on the loan. Values are in months and can be either 36 or 60. |
| 6 | `int_rate` | DOUBLE | 0.0 | 712 | 5.31 … 30.99 | Interest Rate on the loan |
| 7 | `installment` | DOUBLE | 0.0 | 94,350 | 4.93 … 1719.83 | The monthly payment owed by the borrower if the loan originates. |
| 8 | `grade` | VARCHAR | 0.0 | 7 | A … G | LC assigned loan grade |
| 9 | `sub_grade` | VARCHAR | 0.0 | 35 | A1 … G5 | LC assigned loan subgrade |
| 10 | `emp_title` | VARCHAR | 7.4 | 588,977 | 	CFO … 👨‍🍳  | The job title supplied by the Borrower when applying for the loan.* |
| 11 | `emp_length` | VARCHAR | 6.5 | 12 | 1 year … < 1 year | Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years. |
| 12 | `home_ownership` | VARCHAR | 0.0 | 6 | ANY … RENT | The home ownership status provided by the borrower during registration or obtained from the credit report. Our values are: RENT, OWN, MORTGAGE, OTHER |
| 13 | `annual_inc` | DOUBLE | 0.0 | 91,704 | 0.0 … 110000000.0 | The self-reported annual income provided by the borrower during registration. |
| 14 | `verification_status` | VARCHAR | 0.0 | 3 | Not Verified … Verified | Indicates if income was verified by LC, not verified, or if the income source was verified |
| 15 | `issue_d` | VARCHAR | 0.0 | 159 | Apr-2008 … Sep-2018 | The month which the loan was funded |
| 16 | `loan_status` | VARCHAR | 0.0 | 9 | Charged Off … Late (31-120 days) | Current status of the loan |
| 17 | `pymnt_plan` | VARCHAR | 0.0 | 2 | n … y | Indicates if a payment plan has been put in place for the loan |
| 18 | `url` | VARCHAR | 0.0 | 2,751,478 | https://lendingclub.com/… … https://lendingclub.com/… | URL for the LC page with listing data. |
| 19 | `desc` | VARCHAR | 94.4 | 110,475 | 	 Loan for purchase of g… … ~20K total in medical ex… | Loan description provided by the borrower |
| 20 | `purpose` | VARCHAR | 0.0 | 15 | car … wedding | A category provided by the borrower for the loan request. |
| 21 | `title` | VARCHAR | 1.0 | 52,137 | 	credit_card … îîMY FIRST CAR îî | The loan title provided by the borrower |
| 22 | `zip_code` | VARCHAR | 0.0 | 1,040 | 007xx … 999xx | The first 3 numbers of the zip code provided by the borrower in the loan application. |
| 23 | `addr_state` | VARCHAR | 0.0 | 55 | AK … WY | The state provided by the borrower in the loan application |
| 24 | `dti` | DOUBLE | 0.1 | 8,658 | -1.0 … 999.0 | A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income. |
| 25 | `delinq_2yrs` | DOUBLE | 0.0 | 37 | 0.0 … 58.0 | The number of 30+ days past-due incidences of delinquency in the borrower's credit file for the past 2 years |
| 26 | `earliest_cr_line` | VARCHAR | 0.0 | 916 | Apr-1934 … Sep-2015 | The month the borrower's earliest reported credit line was opened |
| 27 | `fico_range_low` | DOUBLE | 0.0 | 51 | 610.0 … 845.0 | The lower boundary range the borrower’s FICO at loan origination belongs to. |
| 28 | `fico_range_high` | DOUBLE | 0.0 | 49 | 614.0 … 850.0 | The upper boundary range the borrower’s FICO at loan origination belongs to. |
| 29 | `inq_last_6mths` | DOUBLE | 0.0 | 29 | 0.0 … 33.0 | The number of inquiries in past 6 months (excluding auto and mortgage inquiries) |
| 30 | `mths_since_last_delinq` | DOUBLE | 51.2 | 206 | 0.0 … 226.0 | The number of months since the borrower's last delinquency. |
| 31 | `mths_since_last_record` | DOUBLE | 84.1 | 165 | 0.0 … 129.0 | The number of months since the last public record. |
| 32 | `open_acc` | DOUBLE | 0.0 | 119 | 0.0 … 101.0 | The number of open credit lines in the borrower's credit file. |
| 33 | `pub_rec` | DOUBLE | 0.0 | 55 | 0.0 … 86.0 | Number of derogatory public records |
| 34 | `revol_bal` | DOUBLE | 0.0 | 100,825 | 0.0 … 2904836.0 | Total credit revolving balance |
| 35 | `revol_util` | DOUBLE | 0.1 | 1,528 | 0.0 … 892.3 | Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit. |
| 36 | `total_acc` | DOUBLE | 0.0 | 189 | 1.0 … 176.0 | The total number of credit lines currently in the borrower's credit file |
| 37 | `initial_list_status` | VARCHAR | 0.0 | 2 | f … w | The initial listing status of the loan. Possible values are – W, F |
| 38 | `out_prncp` | DOUBLE | 0.0 | 364,126 | 0.0 … 40000.0 | Remaining outstanding principal for total amount funded |
| 39 | `out_prncp_inv` | DOUBLE | 0.0 | 360,231 | 0.0 … 40000.0 | Remaining outstanding principal for portion of total amount funded by investors |
| 40 | `total_pymnt` | DOUBLE | 0.0 | 1,622,606 | 0.0 … 63296.877916990896 | Payments received to date for total amount funded |
| 41 | `total_pymnt_inv` | DOUBLE | 0.0 | 1,317,947 | 0.0 … 63296.88 | Payments received to date for portion of total amount funded by investors |
| 42 | `total_rec_prncp` | DOUBLE | 0.0 | 491,382 | 0.0 … 40000.0 | Principal received to date |
| 43 | `total_rec_int` | DOUBLE | 0.0 | 651,388 | 0.0 … 28192.5 | Interest received to date |
| 44 | `total_rec_late_fee` | DOUBLE | 0.0 | 15,261 | -9.499999999999999e-09 … 1484.34 | Late fees received to date |
| 45 | `recoveries` | DOUBLE | 0.0 | 114,505 | 0.0 … 39859.55 | post charge off gross recovery |
| 46 | `collection_recovery_fee` | DOUBLE | 0.0 | 150,185 | 0.0 … 7174.719 | post charge off collection fee |
| 47 | `last_pymnt_d` | VARCHAR | 0.1 | 147 | Apr-2008 … Sep-2018 | Last month payment was received |
| 48 | `last_pymnt_amnt` | DOUBLE | 0.0 | 675,055 | 0.0 … 42192.05 | Last total payment amount received |
| 49 | `next_pymnt_d` | VARCHAR | 59.5 | 109 | Apr-2008 … Sep-2018 | Next scheduled payment date |
| 50 | `last_credit_pull_d` | VARCHAR | 0.0 | 157 | Apr-2009 … Sep-2018 | The most recent month LC pulled credit for this loan |
| 51 | `last_fico_range_high` | DOUBLE | 0.0 | 74 | 0.0 … 850.0 | The upper boundary range the borrower’s last FICO pulled belongs to. |
| 52 | `last_fico_range_low` | DOUBLE | 0.0 | 69 | 0.0 … 845.0 | The lower boundary range the borrower’s last FICO pulled belongs to. |
| 53 | `collections_12_mths_ex_med` | DOUBLE | 0.0 | 17 | 0.0 … 20.0 | Number of collections in 12 months excluding medical collections |
| 54 | `mths_since_last_major_derog` | DOUBLE | 74.3 | 206 | 0.0 … 226.0 | Months since most recent 90-day or worse rating |
| 55 | `policy_code` | DOUBLE | 0.0 | 1 | 1.0 … 1.0 | publicly available policy_code=1 new products not publicly available policy_code=2 |
| 56 | `application_type` | VARCHAR | 0.0 | 2 | Individual … Joint App | Indicates whether the loan is an individual application or a joint application with two co-borrowers |
| 57 | `annual_inc_joint` | DOUBLE | 94.7 | 15,913 | 5693.51 … 7874821.0 | The combined self-reported annual income provided by the co-borrowers during registration |
| 58 | `dti_joint` | DOUBLE | 94.7 | 2,936 | 0.0 … 69.49 | A ratio calculated using the co-borrowers' total monthly payments on the total debt obligations, excluding mortgages and the requested LC loan, divided by the co-borrowers' combined self-reported monthly income |
| 59 | `verification_status_joint` | VARCHAR | 94.9 | 3 | Not Verified … Verified | Indicates if the co-borrowers' joint income was verified by LC, not verified, or if the income source was verified *(в словаре: `verified_status_joint`)* |
| 60 | `acc_now_delinq` | DOUBLE | 0.0 | 10 | 0.0 … 14.0 | The number of accounts on which the borrower is now delinquent. |
| 61 | `tot_coll_amt` | DOUBLE | 3.1 | 15,210 | 0.0 … 9152545.0 | Total collection amounts ever owed |
| 62 | `tot_cur_bal` | DOUBLE | 3.1 | 469,046 | 0.0 … 9971659.0 | Total current balance of all accounts |
| 63 | `open_acc_6m` | DOUBLE | 38.3 | 20 | 0.0 … 18.0 | Number of open trades in last 6 months |
| 64 | `open_act_il` | DOUBLE | 38.3 | 58 | 0.0 … 57.0 | Number of currently active installment trades |
| 65 | `open_il_12m` | DOUBLE | 38.3 | 21 | 0.0 … 25.0 | Number of installment accounts opened in past 12 months |
| 66 | `open_il_24m` | DOUBLE | 38.3 | 34 | 0.0 … 51.0 | Number of installment accounts opened in past 24 months |
| 67 | `mths_since_rcnt_il` | DOUBLE | 40.2 | 459 | 0.0 … 511.0 | Months since most recent installment accounts opened |
| 68 | `total_bal_il` | DOUBLE | 38.3 | 166,981 | 0.0 … 1837038.0 | Total current balance of all installment accounts |
| 69 | `il_util` | DOUBLE | 47.3 | 270 | 0.0 … 1000.0 | Ratio of total current balance to high credit/credit limit on all install acct |
| 70 | `open_rv_12m` | DOUBLE | 38.3 | 30 | 0.0 … 28.0 | Number of revolving trades opened in past 12 months |
| 71 | `open_rv_24m` | DOUBLE | 38.3 | 54 | 0.0 … 60.0 | Number of revolving trades opened in past 24 months |
| 72 | `max_bal_bc` | DOUBLE | 38.3 | 31,478 | 0.0 … 1170668.0 | Maximum current balance owed on all revolving accounts |
| 73 | `all_util` | DOUBLE | 38.3 | 200 | 0.0 … 239.0 | Balance to credit limit on all trades |
| 74 | `total_rev_hi_lim` | DOUBLE | 3.1 | 32,359 | 0.0 … 9999999.0 | Total revolving high credit/credit limit |
| 75 | `inq_fi` | DOUBLE | 38.3 | 34 | 0.0 … 48.0 | Number of personal finance inquiries |
| 76 | `total_cu_tl` | DOUBLE | 38.3 | 73 | 0.0 … 111.0 | Number of finance trades |
| 77 | `inq_last_12m` | DOUBLE | 38.3 | 53 | 0.0 … 67.0 | Number of credit inquiries in past 12 months |
| 78 | `acc_open_past_24mths` | DOUBLE | 2.2 | 66 | 0.0 … 64.0 | Number of trades opened in past 24 months. |
| 79 | `avg_cur_bal` | DOUBLE | 3.1 | 90,930 | 0.0 … 958084.0 | Average current balance of all accounts |
| 80 | `bc_open_to_buy` | DOUBLE | 3.3 | 101,194 | 0.0 … 711140.0 | Total open to buy on revolving bankcards. |
| 81 | `bc_util` | DOUBLE | 3.4 | 1,566 | 0.0 … 339.6 | Ratio of total current balance to high credit/credit limit for all bankcard accounts. |
| 82 | `chargeoff_within_12_mths` | DOUBLE | 0.0 | 12 | 0.0 … 10.0 | Number of charge-offs within 12 months |
| 83 | `delinq_amnt` | DOUBLE | 0.0 | 3,587 | 0.0 … 249925.0 | The past-due amount owed for the accounts on which the borrower is now delinquent. |
| 84 | `mo_sin_old_il_acct` | DOUBLE | 6.2 | 636 | 0.0 … 999.0 | Months since oldest bank installment account opened |
| 85 | `mo_sin_old_rev_tl_op` | DOUBLE | 3.1 | 759 | 1.0 … 999.0 | Months since oldest revolving account opened |
| 86 | `mo_sin_rcnt_rev_tl_op` | DOUBLE | 3.1 | 330 | 0.0 … 547.0 | Months since most recent revolving account opened |
| 87 | `mo_sin_rcnt_tl` | DOUBLE | 3.1 | 258 | 0.0 … 382.0 | Months since most recent account opened |
| 88 | `mort_acc` | DOUBLE | 2.2 | 49 | 0.0 … 94.0 | Number of mortgage accounts. |
| 89 | `mths_since_recent_bc` | DOUBLE | 3.2 | 601 | 0.0 … 661.0 | Months since most recent bankcard account opened. |
| 90 | `mths_since_recent_bc_dlq` | DOUBLE | 77.0 | 203 | 0.0 … 202.0 | Months since most recent bankcard delinquency |
| 91 | `mths_since_recent_inq` | DOUBLE | 13.1 | 28 | 0.0 … 25.0 | Months since most recent inquiry. |
| 92 | `mths_since_recent_revol_delinq` | DOUBLE | 67.2 | 204 | 0.0 … 202.0 | Months since most recent revolving delinquency. |
| 93 | `num_accts_ever_120_pd` | DOUBLE | 3.1 | 47 | 0.0 … 58.0 | Number of accounts ever 120 or more days past due |
| 94 | `num_actv_bc_tl` | DOUBLE | 3.1 | 43 | 0.0 … 50.0 | Number of currently active bankcard accounts |
| 95 | `num_actv_rev_tl` | DOUBLE | 3.1 | 59 | 0.0 … 72.0 | Number of currently active revolving trades |
| 96 | `num_bc_sats` | DOUBLE | 2.6 | 66 | 0.0 … 71.0 | Number of satisfactory bankcard accounts |
| 97 | `num_bc_tl` | DOUBLE | 3.1 | 96 | 0.0 … 86.0 | Number of bankcard accounts |
| 98 | `num_il_tl` | DOUBLE | 3.1 | 158 | 0.0 … 159.0 | Number of installment accounts |
| 99 | `num_op_rev_tl` | DOUBLE | 3.1 | 101 | 0.0 … 91.0 | Number of open revolving accounts |
| 100 | `num_rev_accts` | DOUBLE | 3.1 | 151 | 0.0 … 151.0 | Number of revolving accounts |
| 101 | `num_rev_tl_bal_gt_0` | DOUBLE | 3.1 | 54 | 0.0 … 65.0 | Number of revolving trades with balance >0 |
| 102 | `num_sats` | DOUBLE | 2.6 | 114 | 0.0 … 101.0 | Number of satisfactory accounts |
| 103 | `num_tl_120dpd_2m` | DOUBLE | 6.8 | 7 | 0.0 … 7.0 | Number of accounts currently 120 days past due (updated in past 2 months) |
| 104 | `num_tl_30dpd` | DOUBLE | 3.1 | 5 | 0.0 … 4.0 | Number of accounts currently 30 days past due (updated in past 2 months) |
| 105 | `num_tl_90g_dpd_24m` | DOUBLE | 3.1 | 35 | 0.0 … 58.0 | Number of accounts 90 or more days past due in last 24 months |
| 106 | `num_tl_op_past_12m` | DOUBLE | 3.1 | 32 | 0.0 … 32.0 | Number of accounts opened in past 12 months |
| 107 | `pct_tl_nvr_dlq` | DOUBLE | 3.1 | 851 | 0.0 … 100.0 | Percent of trades never delinquent |
| 108 | `percent_bc_gt_75` | DOUBLE | 3.3 | 257 | 0.0 … 100.0 | Percentage of all bankcard accounts > 75% of limit. |
| 109 | `pub_rec_bankruptcies` | DOUBLE | 0.1 | 13 | 0.0 … 12.0 | Number of public record bankruptcies |
| 110 | `tax_liens` | DOUBLE | 0.0 | 48 | 0.0 … 85.0 | Number of tax liens |
| 111 | `tot_hi_cred_lim` | DOUBLE | 3.1 | 528,539 | 0.0 … 9999999.0 | Total high credit/credit limit |
| 112 | `total_bal_ex_mort` | DOUBLE | 2.2 | 190,653 | 0.0 … 3408095.0 | Total credit balance excluding mortgage |
| 113 | `total_bc_limit` | DOUBLE | 2.2 | 19,214 | 0.0 … 1569000.0 | Total bankcard high credit/credit limit |
| 114 | `total_il_high_credit_limit` | DOUBLE | 3.1 | 187,141 | 0.0 … 2118996.0 | Total installment high credit/credit limit |
| 115 | `revol_bal_joint` | DOUBLE | 95.2 | 65,208 | 0.0 … 1110019.0 | Sum of revolving credit balance of the co-borrowers, net of duplicate balances |
| 116 | `sec_app_fico_range_low` | DOUBLE | 95.2 | 60 | 540.0 … 845.0 | FICO range (high) for the secondary applicant |
| 117 | `sec_app_fico_range_high` | DOUBLE | 95.2 | 54 | 544.0 … 850.0 | FICO range (low) for the secondary applicant |
| 118 | `sec_app_earliest_cr_line` | VARCHAR | 95.2 | 771 | Apr-1963 … Sep-2017 | Earliest credit line at time of application for the secondary applicant |
| 119 | `sec_app_inq_last_6mths` | DOUBLE | 95.2 | 7 | 0.0 … 6.0 | Credit inquiries in the last 6 months at time of application for the secondary applicant |
| 120 | `sec_app_mort_acc` | DOUBLE | 95.2 | 24 | 0.0 … 27.0 | Number of mortgage accounts at time of application for the secondary applicant |
| 121 | `sec_app_open_acc` | DOUBLE | 95.2 | 77 | 0.0 … 82.0 | Number of open trades at time of application for the secondary applicant |
| 122 | `sec_app_revol_util` | DOUBLE | 95.3 | 1,402 | 0.0 … 434.3 | Ratio of total current balance to high credit/credit limit for all revolving accounts |
| 123 | `sec_app_open_act_il` | DOUBLE | 95.2 | 41 | 0.0 … 43.0 | Number of currently active installment trades at time of application for the secondary applicant |
| 124 | `sec_app_num_rev_accts` | DOUBLE | 95.2 | 110 | 0.0 … 106.0 | Number of revolving accounts at time of application for the secondary applicant |
| 125 | `sec_app_chargeoff_within_12_mths` | DOUBLE | 95.2 | 24 | 0.0 … 21.0 | Number of charge-offs within last 12 months at time of application for the secondary applicant |
| 126 | `sec_app_collections_12_mths_ex_med` | DOUBLE | 95.2 | 20 | 0.0 … 23.0 | Number of collections within last 12 months excluding medical collections at time of application for the secondary applicant |
| 127 | `sec_app_mths_since_last_major_derog` | DOUBLE | 98.4 | 177 | 0.0 … 185.0 | Months since most recent 90-day or worse rating at time of application for the secondary applicant |
| 128 | `hardship_flag` | VARCHAR | 0.0 | 2 | N … Y | Flags whether or not the borrower is on a hardship plan |
| 129 | `hardship_type` | VARCHAR | 99.5 | 1 | INTEREST ONLY-3 MONTHS D… … INTEREST ONLY-3 MONTHS D… | Describes the hardship plan offering |
| 130 | `hardship_reason` | VARCHAR | 99.5 | 9 | DISABILITY … UNEMPLOYMENT | Describes the reason the hardship plan was offered |
| 131 | `hardship_status` | VARCHAR | 99.5 | 1 | ACTIVE … COMPLETED | Describes if the hardship plan is active, pending, canceled, completed, or broken |
| 132 | `deferral_term` | DOUBLE | 99.5 | 1 | 3.0 … 3.0 | Amount of months that the borrower is expected to pay less than the contractual monthly payment amount due to a hardship plan |
| 133 | `hardship_amount` | DOUBLE | 99.5 | 7,955 | 0.64 … 943.94 | The interest payment that the borrower has committed to make each month while they are on a hardship plan |
| 134 | `hardship_start_date` | VARCHAR | 99.5 | 28 | Apr-2017 … Sep-2018 | The start date of the hardship plan period |
| 135 | `hardship_end_date` | VARCHAR | 99.5 | 27 | Apr-2017 … Sep-2018 | The end date of the hardship plan period |
| 136 | `payment_plan_start_date` | VARCHAR | 99.5 | 28 | Apr-2017 … Sep-2018 | The day the first hardship plan payment is due. For example, if a borrower has a hardship plan period of 3 months, the start date is the start of the three-month period in which the borrower is allowed to make interest-only payments. |
| 137 | `hardship_length` | DOUBLE | 99.5 | 1 | 3.0 … 3.0 | The number of months the borrower will make smaller payments than normally obligated due to a hardship plan |
| 138 | `hardship_dpd` | DOUBLE | 99.5 | 33 | 0.0 … 37.0 | Account days past due as of the hardship plan start date |
| 139 | `hardship_loan_status` | VARCHAR | 99.5 | 5 | Current … Late (31-120 days) | Loan Status as of the hardship plan start date |
| 140 | `orig_projected_additional_accrued_interest` | DOUBLE | 99.6 | 8,109 | 1.92 … 2680.89 | The original projected additional interest amount that will accrue for the given hardship payment plan as of the Hardship Start Date. This field will be null if the borrower has broken their hardship payment plan. |
| 141 | `hardship_payoff_balance_amount` | DOUBLE | 99.5 | 9,959 | 55.73 … 40306.41 | The payoff balance amount as of the hardship plan start date |
| 142 | `hardship_last_payment_amount` | DOUBLE | 99.5 | 8,063 | 0.01 … 1407.86 | The last payment amount as of the hardship plan start date |
| 143 | `disbursement_method` | VARCHAR | 0.0 | 2 | Cash … DirectPay | The method by which the borrower receives their loan. Possible values are: CASH, DIRECT_PAY |
| 144 | `debt_settlement_flag` | VARCHAR | 0.0 | 2 | N … Y | Flags whether or not the borrower, who has charged-off, is working with a debt-settlement company. |
| 145 | `debt_settlement_flag_date` | VARCHAR | 98.5 | 94 | Apr-2013 … Sep-2018 | The most recent date that the Debt_Settlement_Flag has been set |
| 146 | `settlement_status` | VARCHAR | 98.5 | 2 | ACTIVE … COMPLETE | The status of the borrower’s settlement plan. Possible values are: COMPLETE, ACTIVE, BROKEN, CANCELLED, DENIED, DRAFT |
| 147 | `settlement_date` | VARCHAR | 98.5 | 98 | Apr-2013 … Sep-2018 | The date that the borrower agrees to the settlement plan |
| 148 | `settlement_amount` | DOUBLE | 98.5 | 19,302 | 44.21 … 33601.0 | The loan amount that the borrower has agreed to settle for |
| 149 | `settlement_percentage` | DOUBLE | 98.5 | 1,840 | 0.2 … 521.35 | The settlement amount as a percentage of the payoff balance amount on the loan |
| 150 | `settlement_term` | DOUBLE | 98.5 | 39 | 0.0 … 181.0 | The number of months that the borrower will be on the settlement plan |
