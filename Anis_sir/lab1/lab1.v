module SOP(x,y,z,FS);
  output FS;
  input x, y, z;
  assign FS = y | (~x & z);
endmodule

module POS(x,y,z,FP);
  output FP;
  input x, y, z;
  assign FP = (~x | y) & (y | z);
endmodule

module lab1;
  wire FSop, FPos;   
  reg x, y, z;       
  
  SOP S( x, y, z, FS);   
  POS P( x, y, z, FP);   

  initial begin
    $dumpfile("lab1.vcd");         
    $dumpvars(0, lab1);              

   
    x = 1'b0; y = 1'b0; z = 1'b0; #10;
    x = 1'b0; y = 1'b0; z = 1'b1; #10;
    x = 1'b0; y = 1'b1; z = 1'b0; #10;
    x = 1'b0; y = 1'b1; z = 1'b1; #10;
    x = 1'b1; y = 1'b0; z = 1'b0; #10;
    x = 1'b1; y = 1'b0; z = 1'b1; #10;
    x = 1'b1; y = 1'b1; z = 1'b0; #10;
    x = 1'b1; y = 1'b1; z = 1'b1; #10;
  end

  initial #100 $finish;   
endmodule