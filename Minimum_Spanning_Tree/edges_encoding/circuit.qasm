OPENQASM 2.0;
include "qelib1.inc";
qreg start[3];
qreg end[3];
qreg ancillas[5];
qreg flags[2];
creg classical_start[3];
creg classical_end[3];
creg classical_flags[2];
h start[0];
h start[1];
h start[2];
h end[0];
h end[1];
h end[2];
h flags[0];
h flags[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x end[2];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x end[2];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[2];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[2];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[2];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[2];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[2];
h flags[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx flags[0],ancillas[1],flags[1];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
h flags[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
h start[0];
h start[1];
h start[2];
h end[0];
h end[1];
h end[2];
h flags[0];
h flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[1];
x end[2];
x flags[0];
x flags[1];
h flags[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],ancillas[4];
ccx flags[0],ancillas[4],flags[1];
ccx end[2],ancillas[3],ancillas[4];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
h flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[1];
x end[2];
x flags[0];
x flags[1];
h start[0];
h start[1];
h start[2];
h end[0];
h end[1];
h end[2];
h flags[0];
h flags[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x end[2];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[1];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x start[0];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x end[2];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x start[2];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[2];
x start[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[2];
x start[0];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x start[2];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[2];
x start[1];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x end[0];
x end[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[1];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[1];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[2];
x end[0];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x end[2];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[2];
x end[0];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[0];
x start[2];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
x start[2];
x end[1];
x end[2];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],flags[0];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
x end[1];
x end[2];
x start[2];
h flags[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx flags[0],ancillas[1],flags[1];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
h flags[1];
barrier start[0],start[1],start[2],end[0],end[1],end[2],ancillas[0],ancillas[1],ancillas[2],ancillas[3],ancillas[4],flags[0],flags[1];
h start[0];
h start[1];
h start[2];
h end[0];
h end[1];
h end[2];
h flags[0];
h flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[1];
x end[2];
x flags[0];
x flags[1];
h flags[1];
ccx start[0],start[1],ancillas[0];
ccx start[2],ancillas[0],ancillas[1];
ccx end[0],ancillas[1],ancillas[2];
ccx end[1],ancillas[2],ancillas[3];
ccx end[2],ancillas[3],ancillas[4];
ccx flags[0],ancillas[4],flags[1];
ccx end[2],ancillas[3],ancillas[4];
ccx end[1],ancillas[2],ancillas[3];
ccx end[0],ancillas[1],ancillas[2];
ccx start[2],ancillas[0],ancillas[1];
ccx start[0],start[1],ancillas[0];
h flags[1];
x start[0];
x start[1];
x start[2];
x end[0];
x end[1];
x end[2];
x flags[0];
x flags[1];
h start[0];
h start[1];
h start[2];
h end[0];
h end[1];
h end[2];
h flags[0];
h flags[1];
measure flags[0] -> classical_flags[0];
measure flags[1] -> classical_flags[1];
measure end[0] -> classical_end[0];
measure end[1] -> classical_end[1];
measure end[2] -> classical_end[2];
measure start[0] -> classical_start[0];
measure start[1] -> classical_start[1];
measure start[2] -> classical_start[2];
