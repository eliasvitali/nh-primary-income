# 2020 New Hampshire Primary Results by Township correlated with per-capita income

Inspired by u/mboop127's [post](https://www.reddit.com/r/SandersForPresident/comments/f2qgs5/bernie_won_the_poorest_counties_in_new_hampshire/?ref=share&ref_source=link) of [@MattyBeRad's Tweet](https://twitter.com/MattyBeRad/status/1227568192404496390?s=20). I personally didn't
think it was a great visual representation as the sample size was way too small (there's what? 7 counties in NH?). However it was a great idea
and so I redid it with townships but all credit to @MattyBeRad for thinking this up

## Notes

* Vote margin was calculated as `100*(Sanders - Buttigieg)/(Sanders + Buttigieg)`. I know this could have been done better as it wasn't all Sanders and Buttigieg but I did this quickly and didn't want to figure that out. Very few townships did not have either as the winner
* Per-capita-income is not representative of household income as it includes all age groups (children/dependents and seniors with $0 income)
* t-test was a simple independent t-test. I am not a statistician however and the extent of my stats knowledge doesn't reach far beyond p < 0.05 = statistically significant result
* I will not interpret the results, I will leave that up to you for reasons mentioned in the point above

## Tools Used
* Pandas for data processing
* Sci-kit for linear regression and statistical analysis (if you can even call it that)
* Matplotlib for visualization

## Data Sources
* Primary Results by Township -- [NY Times/The Associated Press](https://www.nytimes.com/interactive/2020/02/11/us/elections/results-new-hampshire-primary-election.html)
* Income by Township - [U.S. Census Bureau](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk)
