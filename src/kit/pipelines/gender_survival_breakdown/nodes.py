# Copyright 2020 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This is a boilerplate pipeline 'gender_survival_breakdown'
generated using Kedro 0.16.4
"""


import matplotlib.pyplot as plt


def gender_survival_breakdown(df):
    """
    Plot the amount of people who survived and who died, segmented by gender.
    """

    df = df.drop(["Ticket", "Cabin"], axis=1)
    # Remove NaN values
    df = df.dropna()

    fig = plt.figure(figsize=(18, 6))

    # create a plot of two subsets, male and female, of the survived variable.
    # After we do that we call value_counts() so it can be easily plotted as a bar graph.
    # 'barh' is just a horizontal bar graph
    df_male = df.Survived[df.Sex == "male"].value_counts().sort_index()
    df_female = df.Survived[df.Sex == "female"].value_counts().sort_index()

    ax1 = fig.add_subplot(121)
    df_male.plot(kind="barh", label="Male", alpha=0.55)
    df_female.plot(kind="barh", color="#FA2379", label="Female", alpha=0.55)
    plt.title("Who Survived? with respect to Gender, (raw value counts) ")
    plt.legend(loc="best")
    ax1.set_ylim(-1, 2)

    # adjust graph to display the proportions of survival by gender
    ax2 = fig.add_subplot(122)
    (df_male / float(df_male.sum())).plot(kind="barh", label="Male", alpha=0.55)
    (df_female / float(df_female.sum())).plot(
        kind="barh", color="#FA2379", label="Female", alpha=0.55
    )
    plt.title("Who Survived proportionally? with respect to Gender")
    plt.legend(loc="best")

    ax2.set_ylim(-1, 2)

    return fig
