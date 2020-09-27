 #!/bin/bash

user='${{ secrets.USER }}'
countrycode='${{ secrets.CODE }}'
pwd='${{ secrets.PWD }}'

user_list=()
code_list=()
pwd_list=()
IFS="#"
for u in ${user[*]}
do
user_list[${#user_list[*]}]=${u}
done
for c in ${code[*]}
do
code_list[${#code_list[*]}]=${c}
done
for p in ${pwd[*]}
do
pwd_list[${#pwd_list[*]}]=${p}
done
user_num=${#user_list[*]}
code_num=${#user_list[*]}
pwd_num=${#pwd_list[*]}
if [ $user_num != $pwd_num != $code_num ];then
echo "个数不对应 用户数$user_num 密码数$pwd_num 区号数$code_num"
exit 1
else
echo "共有 $user_num 个账号，即将开始签到"
fi
for ((i=0;i<$user_num;i++))
do
python3 sign.py <<EOF
${user_list[$i]}
${code_list[$i]}
${pwd_list[$i]}
EOF
done
