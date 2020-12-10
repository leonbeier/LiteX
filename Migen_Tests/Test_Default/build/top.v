/* Machine-generated using Migen */
module top(
    output user_led,
    input clk50
);

reg [25:0] __main___counter = 26'd0;
wire sys_clk;
wire sys_rst;
wire por_clk;
reg platform_int_rst = 1'd1;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign user_led = __main___counter[25];
assign sys_clk = clk50;
assign por_clk = clk50;
assign sys_rst = platform_int_rst;

always @(posedge por_clk) begin
    platform_int_rst <= 1'd0;
end

always @(posedge sys_clk) begin
    __main___counter <= (__main___counter + 1'd1);
    if (sys_rst) begin
        __main___counter <= 26'd0;
    end
end

endmodule
