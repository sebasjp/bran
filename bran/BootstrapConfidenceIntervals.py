import numpy as np

class BootstrapCI:
    
    def __init__(self, alpha, avg = True, q = None):
        
        self.alpha = alpha
        self.avg   = avg
        self.q     = q
    
    def build_estimator_dist(self, arr):
        """
        This function build the estimator's distribution
        
        Args
            avg (boolean): It indicates if it's True mean estimator will be compute
            q (float): It indicates the quantile value to estimate. It just is valid if avg = False
            arr (array): data 
        
        Return
            list that contains the estimator's distribution bootstrap-based approach
        """
        try:
            assert self.avg == (self.q is None), 'avg = True and q = None or avg = False and q different None'
        except AssertionError as error:
            raise

        n = len(arr)
        estimator_i = None
        estimator_list = []
        
        for i in range(100):
            arr_sample = np.random.choice(arr, n, replace = True)
            if self.avg:
                estimator_i = np.mean(arr_sample)
            else:
                estimator_i = np.quantile(arr_sample, self.q)
                
            estimator_list.append(estimator_i)
        
        return estimator_list
        
    def calculate_ci(self, arr):
        """
        This function compute the confidence interval from estimator's distribution
        
        Args
            alpha (float): significance value. The interval is compute with 
                           (1 - alpha) * 100 confidence level
            arr (array): data
            
        Return
            ll, ul (float): lower and upper limit respectivaly of the confidence interval
        """
        
        alpha_med = self.alpha / 2
        estimator_list = self.build_estimator_dist(arr)
        
        ll, ul = np.quantile(estimator_list, [alpha_med, 1 - alpha_med])
        
        return ll, ul
