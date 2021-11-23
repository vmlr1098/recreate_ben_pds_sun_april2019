import streamlit as st
import pandas as pd
import plotly.express as px
import math
import datetime as dt
import quickplots
import matplotlib.pyplot as plt


def jd_to_date(jd):
    """
    Convert Julian Day to date.

    Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet',
        4th ed., Duffet-Smith and Zwart, 2011.

    Parameters
    ----------
    jd : float
        Julian Day

    Returns
    -------
    year : int
        Year as integer. Years preceding 1 A.D. should be 0 or negative.
        The year before 1 A.D. is 0, 10 B.C. is year -9.

    month : int
        Month as integer, Jan = 1, Feb. = 2, etc.

    day : float
        Day, may contain fractional part.

    Examples
    --------
    Convert Julian Day 2446113.75 to year, month, and day.

    #>>> jd_to_date(2446113.75)
    (1985, 2, 17.25)

    """
    jd = jd + 0.5

    F, I = math.modf(jd)
    I = int(I)

    A = math.trunc((I - 1867216.25) / 36524.25)

    if I > 2299160:
        B = I + 1 + A - math.trunc(A / 4.)
    else:
        B = I

    C = B + 1524

    D = math.trunc((C - 122.1) / 365.25)

    E = math.trunc(365.25 * D)

    G = math.trunc((C - E) / 30.6001)

    day = C - E + F - math.trunc(30.6001 * G)

    if G < 13.5:
        month = G - 1
    else:
        month = G - 13

    if month > 2.5:
        year = D - 4716
    else:
        year = D - 4715

    return year, month, day
def days_to_hmsm(days):
    """
    Convert fractional days to hours, minutes, seconds, and microseconds.
    Precision beyond microseconds is rounded to the nearest microsecond.

    Parameters
    ----------
    days : float
        A fractional number of days. Must be less than 1.

    Returns
    -------
    hour : int
        Hour number.

    min : int
        Minute number.

    sec : int
        Second number.

    micro : int
        Microsecond number.

    Raises
    ------
    ValueError
        If `days` is >= 1.

    Examples
    --------
    >>> days_to_hmsm(0.1)
    (2, 24, 0, 0)

    """
    hours = days * 24.
    hours, hour = math.modf(hours)

    mins = hours * 60.
    mins, min = math.modf(mins)

    secs = mins * 60.
    secs, sec = math.modf(secs)

    micro = round(secs * 1.e6)

    return int(hour), int(min), int(sec), int(micro)
class datetime(dt.datetime):
    """
    A subclass of `datetime.datetime` that performs math operations by first
    converting to Julian Day, then back to a `jdutil.datetime` object.

    Addition works with `datetime.timedelta` objects, subtraction works with
    `datetime.timedelta`, `datetime.datetime`, and `jdutil.datetime` objects.
    Not all combinations work in all directions, e.g.
    `timedelta - datetime` is meaningless.

    See Also
    --------
    datetime.datetime : Parent class.

    """

    def __add__(self, other):
        if not isinstance(other, dt.timedelta):
            s = "jdutil.datetime supports '+' only with datetime.timedelta"
            raise TypeError(s)

        days = timedelta_to_days(other)

        combined = datetime_to_jd(self) + days

        return jd_to_datetime(combined)

    def __radd__(self, other):
        if not isinstance(other, dt.timedelta):
            s = "jdutil.datetime supports '+' only with datetime.timedelta"
            raise TypeError(s)

        days = timedelta_to_days(other)

        combined = datetime_to_jd(self) + days

        return jd_to_datetime(combined)

    def __sub__(self, other):
        if isinstance(other, dt.timedelta):
            days = timedelta_to_days(other)

            combined = datetime_to_jd(self) - days

            return jd_to_datetime(combined)

        elif isinstance(other, (datetime, dt.datetime)):
            diff = datetime_to_jd(self) - datetime_to_jd(other)

            return dt.timedelta(diff)

        else:
            s = "jdutil.datetime supports '-' with: "
            s += "datetime.timedelta, jdutil.datetime and datetime.datetime"
            raise TypeError(s)

    def __rsub__(self, other):
        if not isinstance(other, (datetime, dt.datetime)):
            s = "jdutil.datetime supports '-' with: "
            s += "jdutil.datetime and datetime.datetime"
            raise TypeError(s)

        diff = datetime_to_jd(other) - datetime_to_jd(self)

        return dt.timedelta(diff)

    def to_jd(self):
        """
        Return the date converted to Julian Day.

        """
        return datetime_to_jd(self)

    def to_mjd(self):
        """
        Return the date converted to Modified Julian Day.

        """
        return jd_to_mjd(self.to_jd())
def jd_to_datetime(jd):
    """
    Convert a Julian Day to an `jdutil.datetime` object.

    Parameters
    ----------
    jd : float
        Julian day.

    Returns
    -------
    dt : `jdutil.datetime` object
        `jdutil.datetime` equivalent of Julian day.

    Examples
    --------
    #>>> jd_to_datetime(2446113.75)
    datetime(1985, 2, 17, 6, 0)

    """
    year, month, day = jd_to_date(jd)

    frac_days, day = math.modf(day)
    day = int(day)

    hour, min, sec, micro = days_to_hmsm(frac_days)

    return datetime(year, month, day, hour, min, sec, micro)
jd_to_datetime(2458590.50001)
###################################################################

apr15t19_2019 = pd.read_csv('C:\\Users\\valer\\2019_apr_15_to_19.csv')
apr15t19_2019.count
apr17_2019 = apr15t19_2019[(apr15t19_2019['jdate'] > 2458590.49) & (apr15t19_2019['jdate'] < 2458591.5)]
apr17_2019.count
z = (apr17_2019['jdate']).head(10)
#plt.imshow(quickplots.line(z))
print(z)
#plt.xticks(apr17_2019['jdate'], apr17_2019.index.values)
#plt.plot(apr17_2019['last_az_cmd'])
#plt.plot(apr17_2019['last_el_cmd'])
apr17_2019_08h = apr17_2019[(apr17_2019['jdate'] >= 2458590.83333) & (apr17_2019['jdate'] < 2458590.875)]
apr17_2019_08h.count
#plt.xticks(apr17_2019['jdate'])
#plt.plot(apr17_2019_08h['last_az_cmd'])
#plt.show()


#######################################################################

import streamlit as st
import pandas as pd
import plotly.express as px

apr15t19_2019 = pd.read_csv('C:\\Users\\valer\\2019_apr_15_to_19.csv')
apr17_2019 = apr15t19_2019[(apr15t19_2019['jdate'] > 2458590.49) & (apr15t19_2019['jdate'] < 2458591.5)]

#(pd.read_csv('C:\\Users\\valer\\2019_apr_15_to_19.csv')).head()
#2458574.5

st.write(apr17_2019.head())

var_names = list(apr17_2019.columns)
st.sidebar.title("Make a Selection")
x_axis = st.sidebar.selectbox("Select X-Variable", var_names)
y_axis = st.sidebar.selectbox("Select Y-Variable", var_names)



fig2 = px.line(apr17_2019)
#st.line_chart(fig)
#st.plotly_chart(fig)
#fig.show()
#fig = px.line(title=f'Scatterplot of {x_axis} v. {y_axis}')
#st.line_chart(fig2)
(px.line(fig2, x=x_axis, y=y_axis, title=f'Scatterplot of {x_axis} v. {y_axis}')).show()