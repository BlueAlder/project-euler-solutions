#!/bin/bash

cwd=$(basename "$PWD")

if [ $cwd != "project-euler-solutions" ]
then
  echo "Please run this from the root dir"
  exit 1
fi

if [ $# != 1 ]
then
  echo "Please provide 1 argument which is the name of the challenge"
  exit 1
fi

dirname=$(printf "%04d\n" $1)

if [ -d $dirname ]
then
  echo "Challenge Directory already exists"
  exit 1
fi

mkdir $dirname

exit 0
cd $1

cat <<EOF > solution.py
#!/usr/bin/env python3

# Challenge $1

def main():
  print("unimplemented")

if __name__ == "__main__":
  main()

EOF

chmod +x solution.py
