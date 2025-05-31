from builds_data import builds

def pc_build_advisor():

    # Print welcome message
    print("🖥️ Welcome to the PC Build Advisor!")

    # Get user's budget input
    budget = int(input("💰 Enter your budget (in ₹): "))
    print("🎯 Choose your use case:")
    print("1. Gaming\n2. Video Editing\n3. Casual Use")
    use_case_choice = input("Enter your choice (1/2/3): ")

    # Map user choice to use case
    use_cases = {"1": "Gaming", "2": "Video Editing", "3": "Casual Use"}
    use_case = use_cases.get(use_case_choice)

    if not use_case:
        print("❌ Invalid choice. Please restart.")
        return

    platform = None
    if use_case in ["Gaming", "Video Editing"]:
        print("💻 Choose your preferred platform:")
        print("1. Intel\n2. AMD")
        platform_choice = input("Enter your choice (1/2): ")
        platforms = {"1": "Intel", "2": "AMD"}
        platform = platforms.get(platform_choice)
        if not platform:
            print("❌ Invalid platform choice. Please restart.")
            return

    # Find suitable build
    recommended_build = None
    if use_case in ["Gaming", "Video Editing"]:
        options = builds[use_case][platform]
        for option in options:
            if budget >= option["max_budget"]:
                recommended_build = option["build"]
        if recommended_build is None:
            recommended_build = options[0]["build"]
    else:
        options = builds["Casual Use"]
        for option in options:
            if budget >= option["max_budget"]:
                recommended_build = option["build"]
        if recommended_build is None:
            recommended_build = options[0]["build"]

    # Display the build
    print(f"\n🧰 Recommended Build for {use_case} ({platform if platform else 'N/A'}):")
    for part, spec in recommended_build.items():
        if part != "Total":
            print(f"• {part}: {spec}")
    print(f"💵 Estimated Total Cost: ₹{recommended_build['Total']}")

    if budget >= recommended_build['Total']:
        print("✅ This build fits your budget!")
    else:
        print("⚠️ This build exceeds your budget. Consider increasing it or downgrading parts.")

if __name__ == "__main__":
    pc_build_advisor()
