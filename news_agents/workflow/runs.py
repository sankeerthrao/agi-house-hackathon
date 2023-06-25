from news_agents.agents.script_agent import ScriptAgent
from news_agents.agents.sorter_agent import SorterAgent
from news_agents.agents.pitch_agent import PitchAgent
from news_agents.agents.judge_agent import JudgeAgent


def run_main_loop(
    scripter: ScriptAgent, sorter: SorterAgent, pitcher: PitchAgent, judge: JudgeAgent
) -> bool:
    summary = scripter.write_script(
        """Immediately after another media event held the following September, Apple removed almost all mentions of AirPower from its website.[5] There were reportedly several development issues that led to this decision, with heat management, inter-device communication and speed, as well as mechanical and interference issues all being rumored.[6] Reportedly, the main engineering issue came from including coils for two charging standards, as the Apple Watch uses a proprietary non-Qi standard.[7] Blogger John Gruber, known for his close connections with Apple, wrote that he had heard of issues with the device’s design: "Something about the multi-coil design getting too hot — way too hot. There are engineers who looked at AirPower’s design and said it could never work thermally."[8]

AirPower was still mentioned in the packaging of several Apple products, including iPhone XS and iPhone XR,[9] and in January 2019 media outlets reported that AirPower may have entered production.[10] On March 25, 2019, Apple released iOS 12.2 with support for AirPower. On March 26, 2019, Apple shipped the Wireless Charging Case for AirPods featuring AirPower on the packaging. Also in late March, Apple secured a trademark on the AirPower name.[11]

However, on March 29, 2019, Dan Riccio, Apple’s senior vice president of Hardware Engineering, said in a statement emailed to TechCrunch: "After much effort, we’ve concluded AirPower will not achieve our high standards and we have canceled the project."[12] The move was unprecedented for Apple as it had never previously canceled an announced hardware product.[13]"""
    )

    sorter_test = sorter.sort_headlines(
        """Fox News v Tucker Carlson: dispute rumbles on weeks after messy exit
        2023 NCAA baseball bracket: Men's College World Series scores, schedule in Omaha
        Skin moles that grow hair may offer treatment for baldness, study suggests
        Prematch Reading | All the biggest news ahead of tonight's homestand finale against Toronto FC
        News Flash • Hopewell Township, NJ • CivicEngage
        Judge keeps no bond order for Ponte Vedra triple stabbing suspect
        Glastonbury: Watch Lizzo, Lewis Capaldi and Rick Astley perform
        """
    )
