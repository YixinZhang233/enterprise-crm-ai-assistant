from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


NOT_MENTIONED = "Not Mentioned"


class Scenario(str, Enum):
    MEMBERSHIP_TIER_BENEFITS = "membership_tier_benefits"
    MEMBER_DAY_CAMPAIGN = "member_day_campaign"
    EXISTING_CUSTOMER_COMMUNICATION_BENEFITS = "existing_customer_communication_benefits"
    PROSPECT_COMMUNICATION_BENEFITS = "prospect_communication_benefits"
    PROSPECT_NEW_EXISTING_MEMBER_BENEFITS = "prospect_new_existing_member_benefits"
    NEW_CUSTOMER_COMMUNICATION_BENEFITS = "new_customer_communication_benefits"


@dataclass(frozen=True)
class FieldSpec:
    name: str
    description: str


@dataclass(frozen=True)
class ExtractionRecord:
    field: str
    exists: str
    value: str


@dataclass(frozen=True)
class ExtractionResult:
    scenario: Scenario
    records: list[ExtractionRecord]


SCHEMA_REGISTRY: dict[Scenario, list[FieldSpec]] = {
    Scenario.MEMBERSHIP_TIER_BENEFITS: [
        FieldSpec("Information Source Channel", "Where the membership benefit information was found."),
        FieldSpec("Tier Benefit Channel", "The channel where tier benefits are displayed or communicated."),
        FieldSpec("Update Date", "Date when the information was updated or captured."),
        FieldSpec("Membership Tier", "Tier number, level, or segment if explicitly shown."),
        FieldSpec("Membership Tier Name", "Named tier such as Silver, Gold, Platinum, or equivalent mock name."),
        FieldSpec("Tier Qualification Criteria", "Explicit requirements to enter the tier."),
        FieldSpec("Birthday Benefit", "Birthday gift, coupon, points, or service."),
        FieldSpec("Exclusive Service", "Dedicated service, advisor, appointment, or support benefit."),
        FieldSpec("Member Privilege", "Any general privilege attached to the tier."),
        FieldSpec("Tier Retention Criteria", "Requirements to maintain the tier."),
        FieldSpec("Tier Retention Benefit", "Benefits for retaining the tier."),
        FieldSpec("Tier Upgrade Criteria", "Requirements to upgrade."),
        FieldSpec("Tier Upgrade Benefit", "Benefits for upgrading."),
        FieldSpec("Year-End Appreciation Gift", "Year-end care, appreciation gift, or annual thank-you benefit."),
        FieldSpec("VIP Event", "Dinner, event, salon, workshop, or similar invitation."),
        FieldSpec("Other Mechanics", "Other CRM mechanics not covered above."),
        FieldSpec("Other Mechanics Name", "Name of the other mechanic."),
        FieldSpec("Newly Observed Mechanic", "Mechanic not previously observed in historical tracking."),
        FieldSpec("Newly Observed Mechanic Name", "Name of the newly observed mechanic."),
    ],
    Scenario.MEMBER_DAY_CAMPAIGN: [
        FieldSpec("Campaign Channel", "Channel where the member day campaign appears."),
        FieldSpec("Campaign Theme", "Campaign name, topic, or creative theme."),
        FieldSpec("Start Date", "Campaign start date."),
        FieldSpec("End Date", "Campaign end date."),
        FieldSpec("Update Date", "Date when the information was updated or captured."),
        FieldSpec("Store Visit Gift", "Gift for store visit, check-in, or consultation."),
        FieldSpec("Tier Upgrade Acceleration", "Any accelerated tier upgrade mechanic."),
        FieldSpec("Gift With Purchase", "Spend threshold gift or purchase reward."),
        FieldSpec("Points Inflation", "Points value inflation or redemption multiplier."),
        FieldSpec("Historical Points Redemption Gift", "Historical points gift mechanic if shown."),
        FieldSpec("Points Multiplier", "Double points, triple points, or similar."),
        FieldSpec("On-Site Instant Redemption", "Immediate redemption at store or event site."),
        FieldSpec("Points Redemption Gift", "Points-for-gift redemption."),
        FieldSpec("Combined Mechanics", "Combination such as redemption plus gift-with-purchase plus visit gift."),
        FieldSpec("Campaign Key Visual And Message", "Main visual message or stated campaign purpose."),
        FieldSpec("MGM Referral", "Member-get-member referral mechanic."),
        FieldSpec("Other Mechanics", "Other campaign mechanics."),
        FieldSpec("Other Mechanics Name", "Name of other mechanic."),
        FieldSpec("Newly Observed Mechanic", "Mechanic not previously observed in historical tracking."),
        FieldSpec("Newly Observed Mechanic Name", "Name of newly observed mechanic."),
    ],
    Scenario.EXISTING_CUSTOMER_COMMUNICATION_BENEFITS: [
        FieldSpec("Contact Date", "Date when the message reached the customer."),
        FieldSpec("Days Since Last Purchase", "Number of days since the last purchase if stated."),
        FieldSpec("Days Since First Purchase", "Number of days since first purchase if stated."),
        FieldSpec("Membership Tier At Contact", "Tier at the time of contact."),
        FieldSpec("Membership Tier Name At Contact", "Tier name at the time of contact."),
        FieldSpec("Contact Channel", "SMS, email, app push, chat, mini app, or other touchpoint."),
        FieldSpec("Communication Type", "Campaign, service reminder, benefit notice, transactional message, etc."),
        FieldSpec("Communication Topic", "Main topic or subject."),
        FieldSpec("Communication Content", "Core message content."),
        FieldSpec("Purchase Oriented", "Whether the message directs the customer to purchase."),
        FieldSpec("Sales Channel Coverage", "Sales channels promoted or linked by the message."),
        FieldSpec("Archived", "Whether the communication was archived or saved."),
    ],
    Scenario.PROSPECT_COMMUNICATION_BENEFITS: [
        FieldSpec("Contact Date", "Date when the message reached the prospect."),
        FieldSpec("Contact Channel", "SMS, email, app push, chat, mini app, or other touchpoint."),
        FieldSpec("Communication Type", "Lead nurture, welcome, invitation, trial offer, etc."),
        FieldSpec("Communication Topic", "Main topic or subject."),
        FieldSpec("Communication Content", "Core message content."),
        FieldSpec("Purchase Oriented", "Whether the message directs the prospect to purchase."),
        FieldSpec("Sales Channel Coverage", "Sales channels promoted or linked by the message."),
        FieldSpec("Archived", "Whether the communication was archived or saved."),
    ],
    Scenario.PROSPECT_NEW_EXISTING_MEMBER_BENEFITS: [
        FieldSpec("Information Source Channel", "Where the benefit information was found."),
        FieldSpec("Update Date", "Date when the information was updated or captured."),
        FieldSpec("Target Audience", "Prospect, new member, existing member, or mixed audience."),
        FieldSpec("Benefit Name", "Name of the benefit."),
        FieldSpec("Purchase Oriented", "Whether the benefit is tied to purchase."),
        FieldSpec("Sales Channel Coverage", "Sales channels covered by the benefit."),
        FieldSpec("Benefit Validity Period", "Validity duration or expiry if stated."),
    ],
    Scenario.NEW_CUSTOMER_COMMUNICATION_BENEFITS: [
        FieldSpec("Contact Date", "Date when the message reached the new customer."),
        FieldSpec("Days Since First Purchase", "Number of days since first purchase if stated."),
        FieldSpec("Membership Tier At Contact", "Tier at the time of contact."),
        FieldSpec("Membership Tier Name At Contact", "Tier name at the time of contact."),
        FieldSpec("Contact Channel", "SMS, email, app push, chat, mini app, or other touchpoint."),
        FieldSpec("Communication Type", "Welcome, onboarding, repurchase prompt, benefit notice, etc."),
        FieldSpec("Communication Topic", "Main topic or subject."),
        FieldSpec("Communication Content", "Core message content."),
        FieldSpec("Purchase Oriented", "Whether the message directs the new customer to purchase."),
        FieldSpec("Sales Channel Coverage", "Sales channels promoted or linked by the message."),
        FieldSpec("Archived", "Whether the communication was archived or saved."),
    ],
}


def get_schema(scenario: Scenario) -> list[FieldSpec]:
    return SCHEMA_REGISTRY[scenario]
