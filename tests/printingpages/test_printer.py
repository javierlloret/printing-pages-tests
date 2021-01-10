from printingpages.printer import Printer, PrinterError

class PrinterTests:

    printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        message = self.printer.print(25)
        assert message == "Printed 25 pages in 12.50 seconds."

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."

        result = self.printer.print(pages)
        assert result == expected

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = "Printed 11 pages in 3.67 seconds."

        result = fast_printer.print(pages)
        assert result == expected

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(15)
        self.printer.print(225)
