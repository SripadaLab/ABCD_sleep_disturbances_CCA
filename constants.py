# define all variables of interest
cbcl_cols = ['cbcl_scr_syn_anxdep_r', 'cbcl_scr_syn_withdep_r', 'cbcl_scr_syn_somatic_r', 'cbcl_scr_syn_social_r',
             'cbcl_scr_syn_thought_r', 'cbcl_scr_syn_attention_r', 'cbcl_scr_syn_rulebreak_r', 'cbcl_scr_syn_aggressive_r']
nih_cols = ['nihtbx_picvocab_uncorrected', 'nihtbx_flanker_uncorrected', 'nihtbx_list_uncorrected',
            'nihtbx_cardsort_uncorrected', 'nihtbx_pattern_uncorrected', 'nihtbx_picture_uncorrected',
            'nihtbx_reading_uncorrected']
sleep_cols = ['sds_p_ss_dims', 'sds_p_ss_sbd','sds_p_ss_da','sds_p_ss_swtd','sds_p_ss_does','sds_p_ss_shy']
pea_cols = ["pea_ravlt_sd_trial_iv_tc","pea_ravlt_ld_trial_vii_tc","pea_wiscv_trs"]
lmt_cols = ['lmt_scr_num_correct']
upps_cols = ['upps_y_ss_negative_urgency', 'upps_y_ss_lack_of_planning', 'upps_y_ss_sensation_seeking',
             'upps_y_ss_positive_urgency', 'upps_y_ss_lack_of_perseverance', 'pps_y_ss_severity_score']
upps_item_cols = ['upps6_y', 'upps7_y', 'upps11_y', 'upps12_y', 'upps15_y', 'upps16_y', 'upps17_y', 'upps18_y',
                  'upps19_y', 'upps20_y', 'upps21_y', 'upps22_y', 'upps23_y', 'upps24_y', 'upps27_y', 'upps28_y',
                  'upps35_y', 'upps36_y', 'upps37_y', 'upps39_y']
bis_cols = ['bis_y_ss_bis_sum', 'bis_y_ss_bas_rr', 'bis_y_ss_bas_drive', 'bis_y_ss_bas_fs']
sscey_cols = ['srpf_y_ss_ses', 'srpf_y_ss_iiss', 'srpf_y_ss_dfs', 'psb_y_ss_mean', 'fes_y_ss_fc_pr']
sscep_cols = ['psb_p_ss_mean', 'fes_p_ss_fc_pr']
ses_cols = ['reshist_addr1_adi_wsum', 'EdYearsAverage']
pdem_cols = ['demo_comb_income_v2']
pf10_cols = ['PF10_lavaan', 'PF10_INT_lavaan', 'PF10_EXT_lavaan']
ses2_cols = ['ses_fac']
g_cols = ['G_lavaan']
bmi_cols = ['bmi']
screen_cols = ['stq_y_ss_weekday', 'stq_y_ss_weekend']
family_cols = ['FHtotal']
med_cols = ['medhx_ss_4b_p', 'medhx_ss_5b_p']
med_cols_2 = ['medhx_2a', 'medhx_2d']
neigh_crimes_par_cols = ['neighborhood1r_p', 'neighborhood2r_p', 'neighborhood3r_p']
community_cohesion_cols = ['comc_phenx_close_knit_p', 'comc_phenx_help_p', 'comc_phenx_get_along_p', 'comc_phenx_share_values_p',
                           'comc_phenx_trusted_p', 'comc_phenx_skip_p', 'comc_phenx_graffiti_p', 'comc_phenx_disrespect_p',
                           'comc_phenx_fight_p', 'comc_phenx_budget_p']
fitbit_sleep_cols = [
#'fit_ss_sleepperiod_minutes',	# total time in sleep
'fit_ss_wake_minutes',  # time awake during sleep
'fit_ss_wake_count',  # number of awakenings during sleep
'fit_ss_light_minutes',  # minutes of light sleep
'fit_ss_deep_minutes',  # minutes of deep sleep
'fit_ss_rem_minutes'  # minutes of rem sleep
]
bpmt_questions = ['bpmt_q'+str(x) for x in range(1, 19)]
asr_cols = ['asr_scr_perstr_r',
 'asr_scr_anxdep_r',
 'asr_scr_withdrawn_r',
 'asr_scr_somatic_r',
 'asr_scr_thought_r',
 'asr_scr_attention_r',
 'asr_scr_aggressive_r',
 'asr_scr_rulebreak_r',
 'asr_scr_intrusive_r',
]

# get all cbcl item columns
cbcl_item_cols = []
for i in range(1,113):
    if i < 10:
        cbcl_item_cols.append(f'cbcl_q0{i}_p')
    elif i == 56:
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'h']:
            cbcl_item_cols.append(f'cbcl_q{i}{letter}_p')
    else:
        cbcl_item_cols.append(f'cbcl_q{i}_p')


all_cols = (cbcl_cols 
            + cbcl_item_cols
            + nih_cols 
            + pea_cols 
            + lmt_cols 
            + upps_cols
            + upps_item_cols
            + bis_cols 
            + sscey_cols 
            + sscep_cols 
            + ses_cols 
            + pdem_cols 
            + pf10_cols 
            + ses2_cols 
            + g_cols 
            + sleep_cols 
            + bmi_cols 
            + screen_cols
            + family_cols
            + med_cols
            + med_cols_2
            + neigh_crimes_par_cols
           )


# now get latent only and subscale columns subsets
nuisance_cols = ['Age', 'Sex', 'RaceEthnicity', 'HouseholdMaritalStatus']
latent_cols = ['G_lavaan', 'PF10_lavaan', 'PF10_INT_lavaan', 'PF10_EXT_lavaan', 'ses_fac']
merge_cols = ['subjectkey', 'eventname']

# paths to read in raw data
path = "" # path to ABCD-NDAR-Release4.0 ABCDStudyNDA data"
