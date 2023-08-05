import re

from pytest_check import check

from . import services
from .result_formatter import ResultFormatter
from .result_summary import ResultSummary
from .utils import Utils


# -------------------
## Holds the verifyxx() functions
class Verifier:
    # -------------------
    ## returns a copy of the default formatter
    #
    # @return None
    def get_formatter(self):
        # TODO return a copy of the default formatter
        return ResultFormatter()

    # -------------------
    ## verify the actual value is True
    #
    # @param actual       the actual value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify(self, actual, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(True, rs)

        if actual:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is True
    # alias for self.verify()
    #
    # @param actual       the actual value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_true(self, actual, reqids=None, formatter=None):
        self.verify(actual, reqids, formatter)

    # -------------------
    ## verify the actual value is False
    #
    # @param actual       the actual value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_false(self, actual, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(False, rs, is_not=False)

        if not actual:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value equals the expected value
    #
    # @param expected     the expected value
    # @param actual       the actual value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_equal(self, expected, actual, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(expected, rs)

        if actual == expected:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value does not equal the expected value
    #
    # @param expected     the expected value
    # @param actual       the actual value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_not_equal(self, expected, actual, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(expected, rs, is_not=True)

        if actual != expected:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is None
    #
    # @param actual       the actual value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_is_none(self, actual, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(None, rs)

        if actual is None:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is not None
    #
    # @param actual       the actual value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_not_none(self, actual, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(None, rs, is_not=True)

        if actual is not None:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is in the given list
    #
    # @param actual       the actual value
    # @param exp_list     the list of values
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_in(self, actual, exp_list, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(exp_list, rs, prefix='in ')

        if actual in exp_list:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is not in the given list
    #
    # @param actual       the actual value
    # @param exp_list     the list of values
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_not_in(self, actual, exp_list, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_expected(exp_list, rs, prefix='in ', is_not=True)

        if actual not in exp_list:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the left value is less than the right value
    #
    # @param left         the left value
    # @param right        the right value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_lt(self, left, right, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(left, rs)
        self._set_expected(right, rs, prefix='less than ')

        if left < right:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the left value is less than or equal to the right value
    #
    # @param left         the left value
    # @param right        the right value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_le(self, left, right, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(left, rs)
        self._set_expected(right, rs, prefix='less than or equal to ')

        if left <= right:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the left value is greater than the right value
    #
    # @param left         the left value
    # @param right        the right value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_gt(self, left, right, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(left, rs)
        self._set_expected(right, rs, prefix='greater than ')

        if left > right:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the left value is greater than or equal to the right value
    #
    # @param left         the left value
    # @param right        the right value
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_ge(self, left, right, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(left, rs)
        self._set_expected(right, rs, prefix='greater or equal to ')

        if left >= right:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value matches the expected regex pattern
    #
    # @param actual       the actual value
    # @param regex        the regex pattern
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_regex(self, actual, regex, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_regex_expected(regex, rs)

        if re.search(regex, actual):
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value does not matche the expected regex pattern
    #
    # @param actual       the actual value
    # @param regex        the regex pattern
    # @param reqids       (optional) one or more reqids associated with this test
    # @param formatter    (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_not_regex(self, actual, regex, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_regex_expected(regex, rs, is_not=True)

        if not re.search(regex, actual):
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is within the expected value +/- the given tolerance
    #
    # @param expected       the expected value
    # @param actual         the actual value
    # @param abs_tolerance  numberic; the absolute +/- tolerance
    # @param reqids         (optional) one or more reqids associated with this test
    # @param formatter      (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_delta(self, expected, actual, abs_tolerance, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_delta_expected(expected, rs, abs_tolerance)

        if abs(actual - expected) < abs_tolerance:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is outside the expected value +/- the given tolerance
    #
    # @param expected       the expected value
    # @param actual         the actual value
    # @param abs_tolerance  numeric; the absolute +/- tolerance
    # @param reqids         (optional) one or more reqids associated with this test
    # @param formatter      (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_not_delta(self, expected, actual, abs_tolerance, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_delta_expected(expected, rs, abs_tolerance, is_not=True)

        if abs(actual - expected) >= abs_tolerance:
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is within the expected value +/- the given percentage tolerance
    #
    # @param expected       the expected value
    # @param actual         the actual value
    # @param rel_tolerance  numeric; the relative percentage +/- % tolerance
    # @param reqids         (optional) one or more reqids associated with this test
    # @param formatter      (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_delta_pct(self, expected, actual, rel_tolerance, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_delta_expected(expected, rs, rel_tolerance, is_pct=True)

        if abs(actual - expected) < (rel_tolerance / 100.0):
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## verify the actual value is outside the expected value +/- the given percentage tolerance
    #
    # @param expected       the expected value
    # @param actual         the actual value
    # @param rel_tolerance  numeric; the relative percentage +/- % tolerance
    # @param reqids         (optional) one or more reqids associated with this test
    # @param formatter      (optional) formatter object to assist in formatting the incoming values
    # @return None
    def verify_not_delta_pct(self, expected, actual, rel_tolerance, reqids=None, formatter=None):
        rs = self._create_result_summary(reqids, formatter)

        self._set_actual(actual, rs)
        self._set_delta_expected(expected, rs, rel_tolerance, is_pct=True, is_not=True)

        if abs(actual - expected) >= (rel_tolerance / 100.0):
            self._handle_pass(rs)
        else:
            self._handle_fail(rs)

    # -------------------
    ## the verify passed, so save the result
    #
    # @param rs    result summary object
    # @return None
    def _handle_pass(self, rs):
        self._save_result_pass(rs)

    # -------------------
    ## the verify failed, so save the result
    # Note: in IUV mode does nothing.
    # In normal mode gathers the failure information and continues
    #
    # @param rs    result summary object
    # @return None
    def _handle_fail(self, rs):
        self._save_result_fail(rs)

        msg = self._format_fail_msg(rs)

        if services.iuvmode:  # pragma: no cover
            pass
        else:
            with check:  # pragma: no cover
                # TODO should only traceback to test_* script
                raise AssertionError(f'at {rs.location}{msg}')

    # -------------------
    ## save a pass result using the given result summary
    #
    # @param rs    result summary object
    # @return None
    def _save_result_pass(self, rs):
        rs.passed()
        services.proto.add_result(rs)

    # -------------------
    ## save a fail result using the given result summary
    #
    # @param rs    result summary object
    # @return None
    def _save_result_fail(self, rs):
        rs.failed()
        services.proto.add_result(rs)

    # -------------------
    ## create a result summary
    #
    # @param reqids      the requirements impacted by this result
    # @param formatter   the formatter, if any, to use for formatting values
    # @return the result summary object
    def _create_result_summary(self, reqids, formatter):
        location = Utils.get_location()

        # create a results summary and pre-populate it
        rs = ResultSummary()
        rs.location = location
        rs.set_reqids(reqids)
        rs.formatter = formatter
        return rs

    # -------------------
    ## save the actual value to the result summary
    #
    # @param actual   the actual value
    # @param rs       result summary object
    # @return None
    def _set_actual(self, actual, rs):
        rs.format_actual(actual)

    # -------------------
    ## save a formatted version of the expected value to the result summary
    #
    # @param expected   the expected value
    # @param rs         result summary object
    # @param prefix     (optional) a prefix string to use in the formatted value
    # @param suffix     (optional) a suffix string to use in the formatted value
    # @param is_not     (optional) if True, use "not" in the formatter value
    # @return None
    def _set_expected(self, expected, rs, prefix=None, suffix=None, is_not=False):
        rs.format_expected(expected, prefix, suffix, is_not=is_not)

    # -------------------
    ## save a formatted version of the expected regex value to the result summary
    #
    # @param expected   the expected value
    # @param rs         result summary object
    # @param is_not     (optional) if True, use "not" in the formatter value
    # @return None
    def _set_regex_expected(self, expected, rs, is_not=False):
        rs.format_regex_expected(expected, is_not=is_not)

    # -------------------
    ## save a formatted version of the expected delta value to the result summary
    #
    # @param expected   the expected value
    # @param rs         result summary object
    # @param delta      the +/- delta value (may be a percentage)
    # @param is_pct     (optional) delta value is percentage
    # @param is_not     (optional) if True, use "not" in the formatter value
    # @return None
    def _set_delta_expected(self, expected, rs, delta, is_pct=False, is_not=False):
        rs.format_delta_expected(expected, delta, is_pct=is_pct, is_not=is_not)

    # -------------------
    ## generate a formatted fail message based on the result summary content
    #
    # @param rs         result summary object
    # @return None
    def _format_fail_msg(self, rs):
        t = f'({rs.expected_type})'
        line1 = f'Expected {t: <10}: {rs.expected_formatted}'
        t = f'({rs.actual_type})'
        line2 = f'Actual   {t: <10}: {rs.actual_formatted}'
        if services.iuvmode:
            services.harness.iuv.print(line1)
            services.harness.iuv.print(line2)

        msg = f'\n   {line1}\n   {line2}'
        return msg
