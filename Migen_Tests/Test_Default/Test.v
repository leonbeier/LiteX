/* Machine-generated using Migen */
module Test(
	input btn,
	output reg led,
	input sys_clk,
	input sys_rst
);

reg [23:0] counter = 24'd0;


always @(posedge sys_clk) begin
	counter <= (counter + 1'd1);
	if (btn) begin
		led <= counter[23];
	end
	if (sys_rst) begin
		led <= 1'd0;
		counter <= 24'd0;
	end
end

endmodule
