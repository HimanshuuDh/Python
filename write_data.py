def main();
    #open a file
    test_file=open("test.txt","w")

    #data
    int_var=123
    float_var=23.45
    bool_var=True

    #processing
    test_file.write(str(int_var)+"\n")
    test_file.write(str(float_var)+"\n")
    test_file.write(str(bool_var)+"\n")

    #close
    test_file.close()

