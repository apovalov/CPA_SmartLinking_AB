# Smart-Link-II-A-B_Design

A/B experimentation is a method of testing a new feature, a new design or interface variant, a new version of an algorithm, etc. The peculiarity of A/B-tests is that they allow isolating the effect from external factors due to simultaneous operation of two versions of a website or application. They allow you to determine which of the variants is better at achieving the set goals: increasing conversion, average check, duration of a user session, etc.

In the process of A/B experiment, several variants are selected and tested on different groups of users. In the simplest case, variant A ("control" - the current variant) and variant B ("test" - the new variant).

For example, in the case of SmartLink service, half of the users are recommended by the old service - algorithm A (which, let's say, offered random ads), and the other half - by the new algorithm B, which we implemented in the first part of the task. Data on user behavior is then collected and the results are compared. This allows us to conclude which variant has a better effect on user behavior and helps us make a more informed decision about which variant of the algorithm should be rolled out to the entire user population.

A/B tests allow you to make decisions based on data rather than assumptions or guesswork.

Algorithm for conducting an A/B test
1. Formulate a hypothesis: if we do X, it will help solve problem Y, which will affect metrics Z.
2. Design the experiment: fix the expected MDE (minimal detectable effect), measure sensitivity and errors of the I-II kind, determine the sample size (how many days the test lasts).
3. Check the design of the experiment on historical data and/or simulations.
4. Run the experiment.
5. Monitor the progress of the experiment.
6. Analyze the experiment: make a decision about the success of the experiment. save all the insights, ideas, and conclusions discovered during the experiment.


# 1. Splitting

Hash + Salt
In real companies, it's rare to do a single experiment. Usually one experiment is followed by other experiments. And in each A/B experiment, users need to be divided differently.

For example, we are conducting an experiment with website design and we divided users into a control group and a test group. The experiment is over and we conduct the next experiment with product recommendations on the main page of the site. In the new experiment, we want to re-mix the users and split them into new groups A and B so that the results of the last experiment do not affect the next one.

The easiest way to re-mix the users is to add a salt to the user ID and then take a hash from such a compound ID. The salt is some text string unique to each experiment. We get a new "identifier with salt", which we feed to the input of the traffic separation algorithm. If the traffic separation algorithm works correctly, it will separate the identifiers of users with different salts differently.

Often the salt is a random string of a few characters, such as "SjgoithY".

Usually the algorithm for separating users into two groups looks like this:

We add a salt to the user ID
We take the hash from such a compound identifier
For the case of two groups and equal separation, even hashes belong to one group, odd hashes to the other.  For other cases the algorithm looks a bit more complicated, but the principle is the same.


# 2. Statistical test

Statistical criterion - a specific statistical test used to decide whether there is a difference between groups. For example, the popular t-test, which tests whether or not the mean of two samples is different.

The output of each test produces some measure of difference (called a statistic), based on which a p-value is calculated.

The p-value is the probability of getting the same value of the statistic or a more extreme value, assuming the null hypothesis is true.

In the case of a t-test, the null hypothesis is that there is no difference between the averages, and the alternative hypothesis is that the mean of some group is greater.

How do you determine that the probability that the samples are not different is small enough to reject the hypothesis of no difference? This is where the significance level α (alpha) comes in.

The significance level α is the probability of rejecting the null hypothesis when it is true. In other words, it is the threshold for determining the statistical significance of the test results. The most common significance level is 0.05, which means that there is a 5% chance of incorrectly rejecting the null hypothesis.

The t-test is not difficult to calculate. The formula for two independent samples looks like this:

\documentclass{article}
\usepackage{amsmath}

\begin{document}

The t-statistic is calculated as follows:

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

Where:
\begin{itemize}
  \item $\bar{x}_1 - \bar{x}_2$ is the difference in means of the two groups being compared.
  \item The denominator is the root of the sum of squared standard errors of each group, divided by the size of each group.
\end{itemize}

\end{document}
