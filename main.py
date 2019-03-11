from directory_manager import DirectoryManager
from get_parameters import get_user_parameters


if __name__ == "__main__":
    # get parameters from command line
    ftp_website, local_directory, max_depth, refresh_frequency, max_thread_num, excluded_extensions  = get_user_parameters()

    # init directory manager with local directory and maximal depth
    directory_manager = DirectoryManager(ftp_website, local_directory, max_depth, excluded_extensions, max_thread_num)

    # launch the synchronization
    directory_manager.synchronize_directory(refresh_frequency)
