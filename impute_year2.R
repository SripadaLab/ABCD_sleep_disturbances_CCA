baseline = read.csv('baseline_data.csv')
baseline = read.csv('year_2_data.csv')
origpredictors = read.csv('baseline_predictors.csv')$predictors
predictors = read.csv('year_2_predictors.csv')$predictors
#alter predictors to include RaceEthnicity and not the levels
predictors = predictors[!(predictors %in% c("Asian","Black","Hispanic","Other"))]
#predictors = predictors[!(predictors %in% c("nihtbx_list_uncorrected","nihtbx_cardsort_uncorrected","pea_wiscv_trs","demo_comb_income_v2","FHtotal","medhx_ss_4b_p","medhx_ss_5b_p","medhx_2a","medhx_2d"))]
predictors = c(predictors,"RaceEthnicity")

sleep = c("sds_p_ss_dims","sds_p_ss_sbd","sds_p_ss_da","sds_p_ss_swtd","sds_p_ss_does","sds_p_ss_shy")

summary(baseline[,predictors])
summary(baseline[,sleep])

mean(100*colSums(is.na(baseline[,predictors]))/nrow(baseline))

i = rowSums(is.na(baseline[,predictors]))
j = rowSums(is.na(baseline[,sleep]))

drop = j==6

dat = baseline[!drop,c("subjectkey","eventname",sleep,predictors)]
dat$M = factor(dat$M,levels=c(0,1))
dat$RaceEthnicity = factor(dat$RaceEthnicity,levels=c("White","Asian","Black","Hispanic","Other"))
dat$not_married = factor(dat$not_married,levels=c(0,1))
dat$medhx_2a_l = factor(dat$medhx_2a_l,levels=c(0,1))
dat$medhx_2d_l = factor(dat$medhx_2d_l,levels=c(0,1))
dat$medhx_ss_4b_p_l = factor(dat$medhx_ss_4b_p_l,levels=c(0,1,2,3,4,5))
dat$neighborhood1r_p = factor(dat$neighborhood1r_p,levels=c(1,2,3,4,5))
dat$neighborhood2r_p = factor(dat$neighborhood2r_p,levels=c(1,2,3,4,5))
dat$neighborhood3r_p = factor(dat$neighborhood3r_p,levels=c(1,2,3,4,5))

dat$comc_phenx_close_knit_p = factor(dat$comc_phenx_close_knit_p,levels=c(1,2,3,4,5))
dat$comc_phenx_help_p = factor(dat$comc_phenx_help_p,levels=c(1,2,3,4,5))
dat$comc_phenx_get_along_p = factor(dat$comc_phenx_get_along_p,levels=c(1,2,3,4,5))
dat$comc_phenx_share_values_p = factor(dat$comc_phenx_share_values_p,levels=c(1,2,3,4,5))
dat$comc_phenx_trusted_p = factor(dat$comc_phenx_trusted_p,levels=c(1,2,3,4,5))
dat$comc_phenx_skip_p = factor(dat$comc_phenx_skip_p,levels=c(1,2,3,4,5))
dat$comc_phenx_graffiti_p = factor(dat$comc_phenx_graffiti_p,levels=c(1,2,3,4,5))
dat$comc_phenx_disresepct_p = factor(dat$comc_phenx_disrespect_p,levels=c(1,2,3,4,5))
dat$comc_phenx_fight_p = factor(dat$comc_phenx_fight_p,levels=c(1,2,3,4,5))
dat$comc_phenx_budget_p = factor(dat$comc_phenx_budget_p,levels=c(1,2,3,4,5))

mat = dat[,c(sleep, predictors)]

library(mice)

blocks = list(sleep=sleep, predictors=predictors)
predictorMatrix = matrix(c(rep(1,length(sleep)),rep(0,length(predictors)),rep(0,length(sleep)),rep(1,length(predictors))),nrow=2,byrow=T)
seed = 1234

m = mice(mat,m=50,predictorMatrix = predictorMatrix, blocks = blocks, seed= seed, maxit=20)
plot(m)

for (i in 1:50) {
  tmp = complete(m,i)
  tmp$subjectkey = dat$subjectkey
  write.csv(tmp,paste0("imputed_",i,"_2year.csv"),row.names=F)
}
  