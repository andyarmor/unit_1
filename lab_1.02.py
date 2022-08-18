'''
Lab 1.02 - Using the Interpreter
Part 1
Using the interpreter, type in the expressions below. Copy and paste the output into the output column. If the
result is unexpected, note that in the third column.
Section 1
    Input                   Output                          Did it do something unexpected?
a   5 + 2 * 2               9                                       no
b   2/3                     0.6666666666666666                      no
c   2.0 * 1.5               3.0                                     no
d   (2 + 3) * 10            50                                      yes it added a .0 for no reason
e   5.0 // 2                2.0                                     yes, not sure
f   5.0 % 2                 1.0                                     yes (modulo division)

Section 2
    Input                   Output                          Did it do something unexpected?
a   a                       gave an error                         yes
b   'a'                     'a'                                   no

Section 3
    Input                   Output                          Did it do something unexpected?
a   'a + b'                 'a + b'                         no
b   'a' + 'b'               'ab'                            yea

Section 4
    Input                   Output                          Did it do something unexpected?
a   'a' * 'b'               error                           yea
b   'a' * 2                 'aa'                            no

Part 2
Before going to the IDE
1. For each item, predict the data type of the result and enter into the "String/Integer/Float" column.
2. Next, predict the value of the result for each item and enter into it into the "Prediction of Result"
column.

    Expression                  String/Integer/Float        Prediction of Result                Interpreter Result
a   10 * 2                      integer                     20                                  20
b   .5 * 2                      float                       1.0                                 1.0
c   10/2                        float                       5.0                                 5.0
d   10%2                        int                         5                                   0
e   2 ** 3                      int                         6                                   8
f   (2+5)*3                     int                         21                                  21
g   2 + 5 * 3                   int                         17                                  17
h   'ab' + '12' + '3'           str                         'ab123'                             'ab123'
i   x                           none                        error                                error
j   "ab" + "cd"                 str                         "abcd"                                "abcd"
k   'abc' * 2                   str                         'abcabc'                            'abcabc'
l   '1'*2 + '2' * 3             str                         11222                               11222
m   1 * 2 + '3' * 2             none                        erorr                               error
n   'A' ** 2                    none                        error                               error
o   'bc' % 2                    none                        unnavailable                        unnavailable
p   'bc' / 2                    none                        copyright/unavailable               unnavailable

Now go to the IDE
Use the interpreter to evaluate the expressions, write down results in the "Interpreter Result" column.
'''