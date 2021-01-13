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
This is a boilerplate pipeline 'class_gender_survival_breakdown'
generated using Kedro 0.16.4
"""


import matplotlib.pyplot as plt


def clean_raw_data(df):
    df = df.drop(["Ticket", "Cabin"], axis=1)
    # Remove NaN values
    df = df.dropna()
    return df


def gender_class_breakdown(df):
    fig = plt.figure(figsize=(18, 4))
    alpha_level = 0.65

    # building on the previous code, here we create an additional subset with in the gender subset
    # we created for the survived variable. I know, thats a lot of subsets. After we do that we call
    # value_counts() so it it can be easily plotted as a bar graph. this is repeated for each gender
    # class pair.
    ax1 = fig.add_subplot(141)
    female_highclass = df.Survived[df.Sex == "female"][df.Pclass != 3].value_counts()
    female_highclass.plot(
        kind="bar", label="female, highclass", color="#FA2479", alpha=alpha_level
    )
    ax1.set_xticklabels(["Survived", "Died"], rotation=0)
    ax1.set_xlim(-1, len(female_highclass))
    plt.title("Who Survived? with respect to Gender and Class")
    plt.legend(loc="best")

    ax2 = fig.add_subplot(142, sharey=ax1)
    female_lowclass = df.Survived[df.Sex == "female"][df.Pclass == 3].value_counts()
    female_lowclass.plot(
        kind="bar", label="female, low class", color="pink", alpha=alpha_level
    )
    ax2.set_xticklabels(["Died", "Survived"], rotation=0)
    ax2.set_xlim(-1, len(female_lowclass))
    plt.legend(loc="best")

    ax3 = fig.add_subplot(143, sharey=ax1)
    male_lowclass = df.Survived[df.Sex == "male"][df.Pclass == 3].value_counts()
    male_lowclass.plot(
        kind="bar", label="male, low class", color="lightblue", alpha=alpha_level
    )
    ax3.set_xticklabels(["Died", "Survived"], rotation=0)
    ax3.set_xlim(-1, len(male_lowclass))
    plt.legend(loc="best")

    ax4 = fig.add_subplot(144, sharey=ax1)
    male_highclass = df.Survived[df.Sex == "male"][df.Pclass != 3].value_counts()
    male_highclass.plot(
        kind="bar", label="male, highclass", alpha=alpha_level, color="steelblue"
    )
    ax4.set_xticklabels(["Died", "Survived"], rotation=0)
    ax4.set_xlim(-1, len(male_highclass))
    plt.legend(loc="best")

    return fig


def gender_proportion_breakdown(df):
    fig = plt.figure(figsize=(18, 2))
    a = 0.65
    # Step 1
    ax1 = fig.add_subplot(141)
    df.Survived.value_counts().plot(kind="bar", color="blue", alpha=a)
    ax1.set_xlim(-1, len(df.Survived.value_counts()))
    plt.title("Step. 1")

    # Step 2
    ax2 = fig.add_subplot(142, sharey=ax1)
    df.Survived[df.Sex == "male"].value_counts().plot(kind="bar", label="Male")
    df.Survived[df.Sex == "female"].value_counts().plot(
        kind="bar", color="#FA2379", label="Female"
    )
    ax2.set_xlim(-1, 2)
    plt.title("Step. 2 \nWho Survived? with respect to Gender.")
    plt.legend(loc="best")

    return fig
