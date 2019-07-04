from services import mine_tracking
import glob, os





if __name__ == '__main__':

     # Create directories
    if not os.path.exists('input'):
        os.makedirs('input')

    if not os.path.exists('output'):
        os.makedirs('output')



    for log_file in glob.glob("input/*.log"):
        if 'MineTracking' in log_file:
            mine_tracking.count(log_file)